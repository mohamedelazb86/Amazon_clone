from rest_framework import serializers
from .models import Product,Brand

class ProductListSerailzers(serializers.ModelSerializer):
    brand=serializers.StringRelatedField()
    class Meta:
        model=Product
        fields='__all__'
class ProductDetailSerailizers(serializers.ModelSerializer):
    brand=serializers.StringRelatedField()
    class Meta:
        model=Product
        fields='__all__'

        

class BrandListSerailizers(serializers.ModelSerializer):
    class Meta:
        model=Brand
        fields='__all__'
class BrandDetailSerailizers(serializers.ModelSerializer):
    class Meta:
        model=Brand
        fields='__all__'