from django.shortcuts import render
from django.db.models import Count
from .models import Settings
from products.models import Brand,Product,Review



def home(request):
    brands=Brand.objects.all()[:10].annotate(product_count=Count('product_brand'))

    context={
        'brands':brands,

    }
  
    
    return render(request,'settings/home.html',context)


