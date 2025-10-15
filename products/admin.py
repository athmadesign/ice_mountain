from django.contrib import admin
from .models import Product

# Register your models here.

@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'sale_price', 'stock', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)
    prepopulated_fields = {'slug': ('name',)}