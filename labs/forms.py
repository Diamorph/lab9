from django import forms
from .models import Restaurants

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class Restaurants_Form(forms.Form):
    image = forms.ImageField()
