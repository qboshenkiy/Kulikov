from django.shortcuts import render
from .models import Product
# Create your views here.
def index(requsets):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(requsets, 'index.html', context )