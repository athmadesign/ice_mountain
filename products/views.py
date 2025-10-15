from django.shortcuts import render
from .models import Product


# Create your views here.
def products(request):
    products = Product.objects.all().order_by('-created_at')
    context = {
        'products': products }
    return render(request, 'core/products.html', context)   