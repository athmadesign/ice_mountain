from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.products, name='products'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),

]