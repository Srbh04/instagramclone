from django.contrib import admin

# Register your models here.
from .models import Users,UserData

admin.site.register(Users)

admin.site.register(UserData)