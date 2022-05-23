from dataclasses import field
from django import forms
from .models import *


class AddDayForm(forms.ModelForm):
  class Meta:
    model = AddDay
    fields = ['user','text','album']