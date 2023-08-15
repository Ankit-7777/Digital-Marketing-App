from django.contrib import admin
from students.models import UserEnquiry


class contactAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'phone','email','city','text')

# Register your models here.
admin.site.register(UserEnquiry,contactAdmin)



