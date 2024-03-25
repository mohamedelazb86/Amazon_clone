from django.urls import path
from .views import ProductDetail,ProductList,BrandDetail,BrandList
from .api import ProductDetailapi,ProductListapi,BrandDetailapi,BrandListApi

urlpatterns = [
    path('brands',BrandList.as_view()),
    path('<slug:slug>/brands',BrandDetail.as_view()),
    path('',ProductList.as_view()),
    path('<slug:slug>',ProductDetail.as_view()),

    # aapi
    path('api/list',ProductListapi.as_view()),
    path('api/list/<int:pk>',ProductDetailapi.as_view()),

    path('api/list/brands',BrandListApi.as_view()),
    path('api/list/brands/<int:pk>',BrandDetailapi.as_view()),

]
