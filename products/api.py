from .serializers import ProductDetailSerailizers,ProductListSerailzers
from .serializers import BrandListSerailizers,BrandDetailSerailizers
from rest_framework import generics
from .models import Product,Brand
from .paginations import Mypagination
from django_filters.rest_framework import DjangoFilterBackend

class ProductListapi(generics.ListAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductListSerailzers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['price',]

class ProductDetailapi(generics.RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductDetailSerailizers
    

class BrandListApi(generics.ListAPIView):
    queryset=Brand.objects.all()
    serializer_class=BrandListSerailizers
    pagination_class=Mypagination

class BrandDetailapi(generics.RetrieveAPIView):
    queryset=Brand.objects.all()
    serializer_class=BrandDetailSerailizers