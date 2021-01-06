from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Product


class ProductView(LoginRequiredMixin, View):
    login_url = '/login?redirect_to=prod'
    redirect_field_name = 'redirect_to'
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'prod.html', locals())


class CartView(View):
    def get(self, request):
        return render(request, 'cart.html', locals()
        )


class AddCartView(View):
    def get(self, request, pid):
        products = Product.objects.get(id=pid)
        return render(request, 'add_cart.html', locals())
        # return HttpResponse(id)