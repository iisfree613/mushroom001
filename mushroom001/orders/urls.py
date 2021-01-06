from django.urls import path

from .views import ProductView, CartView, AddCartView

urlpatterns = [
    path('prod', ProductView.as_view(), name='prod'),
    path('cart', CartView.as_view(), name='cart'),
    path('add_cart/<int:id>', AddCartView.as_view(), name='add_cart'),
]