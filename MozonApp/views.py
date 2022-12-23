from django.shortcuts import render
from .models import *
from django.views import View

# Create your views here.

class ProductListView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'productlist.html', 
                      context={'products': Product.objects.all()})