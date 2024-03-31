from django.shortcuts import render
from django.db.models import Count
from .models import Settings
from products.models import Brand,Product,Review



def home(request):
    brands=Brand.objects.all()[:10].annotate(product_count=Count('product_brand'))
    sale_product=Product.objects.filter(flag='Sale')[:10]
    new_product=Product.objects.filter(flag='New')
    feature_product=Product.objects.filter(flag='Feature_product')

    context={
        'brands':brands,
        'sale_product':sale_product,
        'new_product':new_product,
        'feature_product':feature_product

    }
  
    
    return render(request,'settings/home.html',context)


