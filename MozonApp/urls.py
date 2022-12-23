from django.urls import path
from .views import *

urlpatterns = [
    path('', ProductListView.as_view(), name="product-list"),
    path('add/', OrderCreateView.as_view(), name="order-create"),
    path('orderlist/', OrederListView.as_view(), name="order-list")
]
