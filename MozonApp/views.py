<<<<<<< HEAD
from django.shortcuts import render
from .models import Manufacturer, Сategory, Product, Order
from django.views import View
from . import forms
=======
from django.shortcuts import render, redirect
from .models import *
from django.views import View
from .forms import *
>>>>>>> origin/main

# Create your views here.

class ProductListView(View):
    def get(self, request, *args, **kwargs):
        objs = Product.objects.all()
        objs_photo = [i.picture.url for i in objs]
        return render(request, 'productlist.html', 
<<<<<<< HEAD
                      context={'products': zip(objs, objs_photo), 'form': forms.ProductForm})

    def post(self, request):
        data = forms.ProductForm(request.POST, request.FILES)
        if data.is_valid():
            model = Product.objects.create(
                name = data.cleaned_data["name"],
                cost = data.cleaned_data["cost"],
                specifications = data.cleaned_data["specifications"],
                description = data.cleaned_data["description"],
                manufacturer = data.cleaned_data["manufacturer"],
                picture = data.cleaned_data["picture"],
                category = data.cleaned_data["category"],
            )

            model.save()
            return self.get(request)
        else:
            return self.get(request)
=======
                      context={'products': Product.objects.all()})
        
class OrderCreateView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'ordercreate.html', context={'form': OrderForm()})
    
    def post(self, request, *args, **kwargs):
        form = OrderForm(data=request.POST)
        if form.is_valid():
            model = Order.objects.create(
            product = form.cleaned_data['product'],
            products_count = form.cleaned_data['products_count'],
            person_name = form.cleaned_data['person_name'],
            phone = form.cleaned_data['phone'],
            price = form.cleaned_data['product'].cost * form.cleaned_data['products_count']
            )
            model.save()
            return redirect('http://127.0.0.1:8000/')
        return self.get(request)    
    
class OrederListView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'orderlist.html', 
                      context={'orders': Order.objects.all()})
>>>>>>> origin/main
