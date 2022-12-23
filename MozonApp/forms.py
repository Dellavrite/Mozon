from django import forms
from . import models


class ProductForm(forms.Form):
    name = forms.CharField()
    cost = forms.IntegerField()
    specifications = forms.CharField()
    description = forms.CharField()
    manufacturer = forms.ModelChoiceField(models.Manufacturer.objects)
    picture = forms.ImageField()
    category = forms.ModelChoiceField(models.Сategory.objects)
    