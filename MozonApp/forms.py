from django import forms
from django.forms import ModelChoiceField
from .models import *


class OrderForm(forms.Form):
    product = ModelChoiceField(label="Продукт", queryset=Product.objects.all(), to_field_name="name")
    products_count = forms.IntegerField(label="Количество")
    person_name = forms.CharField(label="ФИО")
    phone = forms.CharField(label="Номер телефона", widget=forms.NumberInput)
    