from django.contrib import admin
from . models import movie
from .models import actor

# Register your models here.

admin.site.register(movie)
admin.site.register(actor)