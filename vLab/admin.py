from django.contrib import admin
from vLab.models import User,Lab_type,Lab

# Register your models here.

class UserAdmin(admin.ModelAdmin):
	list_display = ('user_firstname', 'user_lastname', 'user_vlab', 'user_created')

class LabAdmin(admin.ModelAdmin):
	list_display = ('lab_name','lab_free','lab_type','lab_link','lab_updated')

admin.site.register(User,UserAdmin)
admin.site.register(Lab_type)
admin.site.register(Lab,LabAdmin)
