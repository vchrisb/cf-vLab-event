#from django import forms
from django.forms import ModelForm
from vLab.models import User,Lab_type

class UserForm(ModelForm):
	class Meta:
		model = User
		fields = '__all__'
		labels = {
			'user_firstname': ('Firstname'),
			'user_lastname': ('Lastname'),
			'user_email': ('E-Mail'),
			'user_vlab': ('vLab'),
		}
