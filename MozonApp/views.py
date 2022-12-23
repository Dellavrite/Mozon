from django.shortcuts import render
from .models import Manufacturer, Сategory, Product, Order
from django.views import View
from . import forms

# Create your views here.

class ProductListView(View):
    def get(self, request, *args, **kwargs):
        objs = Product.objects.all()
        objs_photo = [i.picture.url for i in objs]
        return render(request, 'productlist.html', 
                      context={'products': zip(objs, objs_photo), 'form': forms.ProductForm})

    def post(self, request):
        data = forms.ProductForm(request.POST)
        model = Product.objects.create()

        model.name = data.cleaned_data["name"]
        model.cost = data.cleaned_data["cost"]
        model.specifications = data.cleaned_data["specifications"]
        model.description = data.cleaned_data["description"]      
        model.manufacturer = data.cleaned_data["manufacturer"]    
        model.picture = data.cleaned_data["picture"]
        model.category = data.cleaned_data["category"]

        model.save()
