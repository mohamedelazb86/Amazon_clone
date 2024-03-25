from django.shortcuts import render
from .models import Product,Brand
from django.views.generic import ListView,DetailView


class ProductList(ListView):
    model=Product
    paginate_by=24

class ProductDetail(DetailView):
    model=Product

class BrandList(ListView):
    model=Brand
    paginate_by=30

class BrandDetail(DetailView):
    model=Brand

