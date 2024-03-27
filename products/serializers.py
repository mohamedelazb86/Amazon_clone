from rest_framework import serializers
from .models import Product,Brand,Product_Image,Review

class ImageSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Product_Image
        fields='__all__'

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields='__all__'

class ProductListSerailzers(serializers.ModelSerializer):
    brand=serializers.StringRelatedField()
    class Meta:
        model=Product
        fields='__all__'
class ProductDetailSerailizers(serializers.ModelSerializer):
    brand=serializers.StringRelatedField()
    reviews=ReviewSerializers(source='review_product',many=True)
    image=ImageSerailizer(source='image_product',many=True)
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