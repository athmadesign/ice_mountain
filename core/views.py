from django.shortcuts import render
from .models import Slider

# Create your views here.
def index(request):
    sliders = Slider.objects.filter(is_active=True).order_by('-created_at')
    context = {
        'sliders': sliders
    }
    return render(request, 'core/index.html', context)

def about(request):
    return render(request, 'core/about.html')


def contact(request):
    return render(request, 'core/contact.html')