from django.contrib import admin
from auth_.models import Profile
from auth_.models import MainUser

# Register your models here.

admin.site.register(MainUser)
admin.site.register(Profile)
