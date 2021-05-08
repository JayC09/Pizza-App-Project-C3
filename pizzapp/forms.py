from django import forms
from django.forms import ModelForm

from .models import *

class PizzaForm(forms.ModelForm):
    class Meta:
        model = pizza
        fields = '__all__'