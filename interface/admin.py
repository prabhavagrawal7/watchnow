from django.contrib import admin
from .models import Movies, Profile, Contact
# Register your models here.
admin.site.register(Movies)
admin.site.register(Profile)
admin.site.register(Contact)