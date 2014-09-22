from django.conf.urls import patterns, url

from vLab import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
)
