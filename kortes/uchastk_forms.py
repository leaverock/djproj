from django import forms
from django.forms import ModelForm
from track.models import UchSTRUCT


class UchEditForm(forms.Form):
    DorNam = forms.CharField(label='Your name', max_length=100)

