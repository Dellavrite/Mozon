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
