from django.shortcuts import render, redirect
from .models import *
from django.views import View
from .forms import *

# Create your views here.

class ProductListView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'productlist.html', 
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