from django.shortcuts import render, redirect
from .models import Manufacturer, Сategory, Product, Order
from django.views import View
from . import forms, models

# Create your views here.

class ProductListView(View):
    def get(self, request, *args, **kwargs):
        objs = Product.objects.all()
        objs_photo = [i.picture.url for i in objs]
        return render(request, 'productlist.html', 
                      context={'products': zip(objs, objs_photo), 'form': forms.ProductModelForm})

    def post(self, request):
        data = forms.ProductModelForm(request.POST, request.FILES)
        if data.is_valid():
            data.save()
            return self.get(request)
        else:
            return self.get(request)


class ProductView(View):
    def get(self, request, pk):
        model = models.Product.objects.get(pk=pk)
        form = forms.ProductModelForm(instance=model)

        return render(request, 'products/product.html', context={
            'form': form
        })
    
    def post(self, request, pk):
        model = models.Product.objects.get(pk=pk)
        form = forms.ProductModelForm(request.POST, request.FILES, instance=model)
        form.save()

        return redirect('/')


def deleteProduct(request, pk):
    model = models.Product.objects.get(pk=pk)
    model.delete()
    return redirect('/')


class OrderCreateView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'ordercreate.html', context={'form': forms.OrderForm()})

    def post(self, request, *args, **kwargs):
        form = forms.OrderForm(data=request.POST)
        if form.is_valid():
            model = Order.objects.create(
            product = form.cleaned_data['product'],
            products_count = form.cleaned_data['products_count'],
            person_name = form.cleaned_data['person_name'],
            phone = form.cleaned_data['phone'],
            price = form.cleaned_data['product'].cost * form.cleaned_data['products_count']
            )
            model.save()
            return redirect('/')
        return self.get(request)


class OrederListView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'orderlist.html', 
                      context={'orders': Order.objects.all()})
