from django.shortcuts import render
from .models import Product
# Create your views here.
def home(request):
    template= 'index.html'
    return render(request, template)
def all(request):
    products= Product.objects.all()
    context = {'products': products}
    template ='shop.html'
    return render(request, template, context)
