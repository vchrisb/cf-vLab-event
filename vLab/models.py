from django.db import models
from django import forms

# Create your models here.
class Lab_type(models.Model):
	lab_name = models.CharField(max_length=200)
	def __str__(self):
		return self.lab_name


class User(models.Model):
	user_firstname = models.CharField(max_length=200)
	user_lastname = models.CharField(max_length=200)
	user_email = models.EmailField()
	user_vlab = models.ForeignKey(Lab_type)
	user_created = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.user_lastname

class Lab(models.Model):
	lab_type = models.ForeignKey(Lab_type)
	lab_name = models.CharField(max_length=200)
	lab_link = models.CharField(max_length=200)
	lab_free = models.BooleanField(default=True)
	lab_updated = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.lab_link

