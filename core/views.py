from django.shortcuts import render
from .models import Slider
from products.models import Product

# Create your views here.
def index(request):
    sliders = Slider.objects.filter(is_active=True).order_by('-created_at')
    products = Product.objects.all().order_by('-created_at')[:8]  # Fetch latest 8 products
    context = {
        'sliders': sliders, 'products': products
    }
    return render(request, 'core/index.html', context)

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')