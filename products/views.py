from django.shortcuts import render,redirect
from .models import Product,Brand,Review,Product_Image
from django.views.generic import ListView,DetailView
from django.db.models import Count,Q
from products.models import Product,Review


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
    
    
def mydebug(request):

    # number ---------------------
    #data=Product.objects.all()
    #data=Product.objects.filter(price=21.18)
    #data=Product.objects.filter(price__gt=95)
   # data=Product.objects.filter(price__gte=85)
    #data=Product.objects.filter(price__lt=80)
   # data=Product.objects.filter(price__lte=90)
    #data=Product.objects.filter(price__range=(80,100))

    #   relations -----------------------
   # data=Product.objects.filter(brand__name='Kerri Cohen')
    #data=Product.objects.filter(brand__slug='mary-kelley')
    #data=Product.objects.filter(brand__id__gt=20)

    # text-----------------------------
    #data=Product.objects.filter(name__contains='Mary')
    #data=Product.objects.filter(name__startswith='Brian')
    #data=Product.objects.filter(name__endswith='Ramirez')

    #data=Product.objects.filter(price__isnull=True)

    #   data ----------------------
    #data=Product.objects.filter(date__year=2022)
    #data=Product.objects.filter(date__month=12)
    #data=Product.objects.filter(date__days=23)

    # complex
    #data=Product.objects.filter(price=85,name='4555')

    #data=Product.objects.filter(price=48.25).filter(slug='william-martinez')
    # data=Product.objects.filter(
    #     ~Q(price=21)&
    #     Q(slug='william-martinez')
    # )
    # data=Product.objects.earliest('name')
    # data=Product.objects.latest('name')
    data=Product.objects.select_related('brand').all()
    data=Product.objects.prefetch_related('brand').all()





    
    return render(request,'products/debug.html',{'data':data})
def add_review(request,slug):
    product=Product.objects.get(slug=slug)
    review=request.POST['rate']
    rate=request.POST['rating']
    Review.objects.create(
        user=request.user,
        product=product,
        rate=rate,
        review=review

    )
    return redirect(f'/products/{product.slug}')
    


    
    
    

    

