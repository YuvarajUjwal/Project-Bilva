from django import forms
from .models import *

class TagForm(forms.ModelForm):
    class Meta:
        model = Tags
        fields = ['category']

class EnquireForm(forms.ModelForm):
    class Meta:
        model = Enquire
        fields = ['name', 'phone', 'email', 'message']

class ImageForm(forms.ModelForm):
    class Meta:
        model = Galeries
        fields = ['tag','photo']