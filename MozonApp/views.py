from django.shortcuts import render
from .models import Manufacturer, Сategory, Product, Order
from django.views import View

# Create your views here.

class ProductListView(View):
    def get(self, request, *args, **kwargs):
        objs = Product.objects.all()
        objs_photo = [i.picture.url for i in objs]
        return render(request, 'productlist.html', 
                      context={'products': Product.objects.all()})
