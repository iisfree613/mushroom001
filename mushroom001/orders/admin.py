from django.contrib import admin

from .models import Product, Order, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc')


@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'desc', 'price', 'model',
                    'created', 'updated')
    list_per_page = 20


@admin.register(Order)
class BookingsAdmin(admin.ModelAdmin):
    list_display = ('order_id',
                    'generator',
                    'to_user',
                    'total_price',
                    'order_status',
                    )
    list_per_page = 20
