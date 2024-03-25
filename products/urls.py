from django.urls import path
from .views import ProductDetail,ProductList,BrandDetail,BrandList

urlpatterns = [
    path('brands',BrandList.as_view()),
    path('<slug:slug>/brands',BrandDetail.as_view()),
    path('',ProductList.as_view()),
    path('<slug:slug>',ProductDetail.as_view()),
]
