# forms.py

from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import *




class AudioForm(forms.ModelForm):
    class Meta:
        model=Audio_store
        fields=['record']
