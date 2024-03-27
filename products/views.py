from django.shortcuts import render
from .models import Product,Brand,Review,Product_Image
from django.views.generic import ListView,DetailView
from django.db.models import Count


class ProductList(ListView):
    model=Product
    paginate_by=24

class ProductDetail(DetailView):
    model=Product

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)          # one object    detail
        context["reviews"] =Review.objects.filter(product=self.get_object()).order_by('-id')[:3]
        context["images"] = Product_Image.objects.filter(product=self.get_object())
        context["related"] = Product.objects.filter(brand=self.get_object().brand)
        return context
    

class BrandList(ListView):
    model=Brand
    paginate_by=30
    queryset=Brand.objects.annotate(product_count=Count('product_brand'))

# class BrandDetail(DetailView):
#     model=Brand

#     def get_context_data(self, **kwargs) :
#         context = super().get_context_data(**kwargs)   # one brand only detail
#         context["related"] = Product.objects.filter(brand=self.get_object())
#         return context
    
class BrandDetail(ListView):
    model=Product
    template_name='products/brand_detail.html'
    paginate_by=5

    def get_queryset(self):
        brand=Brand.objects.get(slug=self.kwargs['slug'])
        queryset=super().get_queryset().filter(brand=brand)
        
        return queryset
    
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["brands"] = Brand.objects.filter(slug=self.kwargs['slug']).annotate(product_count=Count('product_brand'))[0]
        return context
    
    
    

    

