from django.shortcuts import render, get_object_or_404
from .models import Product


def products(request):
    products = Product.objects.all().order_by('-created_at')
    context = {
        'products': products }
    return render(request, 'core/products.html', context)   


def product_detail(request, slug):
    product_details = get_object_or_404(Product, slug=slug)
    context = {
        'product_details': product_details }
    return render(request, 'core/product_detail.html', context)