from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from django.http import HttpResponseRedirect
from vLab.forms import UserForm
from vLab.models import User, Lab, Lab_type
from django.template import RequestContext

# Create your views here.
def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            new_user = form.save(commit=False)
            # redirect to a new URL:
            try:
                lab = Lab.objects.filter(lab_type=new_user.user_vlab,lab_free=True).first()
            except:
                raise Http404
            if not lab:
                return HttpResponse("No lab of selected type is free!")
            lab.lab_free = False
            lab.save()
            new_user.save()
            return HttpResponseRedirect(lab.lab_link)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserForm()

    return render(request, 'vLab/input.html', {'form': form},context_instance=RequestContext(request))
