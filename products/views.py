from django.shortcuts import render
from .models import Product,Brand,Review,Product_Image
from django.views.generic import ListView,DetailView


class ProductList(ListView):
    model=Product
    paginate_by=24

class ProductDetail(DetailView):
    model=Product

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)          # one object    detail
        context["reviews"] =Review.objects.filter(product=self.get_object()).order_by('-id')[:3]
        context["images"] = Product_Image.objects.filter(product=self.get_object())
        return context
    

class BrandList(ListView):
    model=Brand
    paginate_by=30

class BrandDetail(DetailView):
    model=Brand

