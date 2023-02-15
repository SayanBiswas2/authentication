from django import forms
from .models import userinfo

class FormAuthForm(forms.ModelForm):
  class Meta:
    model= userinfo
    fields=["email","password"]