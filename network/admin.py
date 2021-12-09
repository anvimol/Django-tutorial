from django.contrib import admin
from django.contrib.admin.decorators import register
from . import models

# Register your models here.
admin.site.register(models.Post)
