from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(AddDay)
class AddDayAdmin(admin.ModelAdmin):
  list_display = ['id','user','text']
