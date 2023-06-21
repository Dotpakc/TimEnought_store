from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Product

# Create your views here.

class ShopList(ListView):
    model = Product
    
class ProductDetail(DetailView):
    model = Product
    
    
    
    