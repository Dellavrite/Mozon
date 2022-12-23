from django import forms
from django.forms import ModelChoiceField
from .models import *
from . import models


class ProductForm(forms.Form):
    name = forms.CharField()
    cost = forms.IntegerField()
    specifications = forms.CharField()
    description = forms.CharField()
    manufacturer = forms.ModelChoiceField(models.Manufacturer.objects)
    picture = forms.ImageField()
    category = forms.ModelChoiceField(models.Сategory.objects)


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = '__all__'


class OrderForm(forms.Form):
    product = ModelChoiceField(label="Продукт", queryset=Product.objects.all(), to_field_name="name")
    products_count = forms.IntegerField(label="Количество")
    person_name = forms.CharField(label="ФИО")
    phone = forms.CharField(label="Номер телефона", widget=forms.NumberInput)
    
