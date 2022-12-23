from django.urls import path, include
from .views import ProductListView, OrderCreateView, OrederListView
from . import views

product_url_patterns = [
    path('', ProductListView.as_view(), name="product-list"),
    path('<int:pk>/delete/', views.deleteProduct),
    path('<int:pk>/', views.ProductView.as_view()),
]

urlpatterns = [
    path('', include(product_url_patterns)),
    path('add/', OrderCreateView.as_view(), name="order-create"),
    path('orderlist/', OrederListView.as_view(), name="order-list")
]
