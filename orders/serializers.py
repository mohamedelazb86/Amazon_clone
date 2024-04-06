from rest_framework import serializers
from .models import Cart,CartDetail,Order,OrderDetail


class OrderDetailserializers(serializers.ModelSerializer):
    class Meta:
        model=OrderDetail
        fields='__all__'
class OrderSerializers(serializers.ModelSerializer):
    order_detail=OrderDetailserializers(source='detail_order',many=True)
    class Meta:
        model=Order
        fields='__all__'

class CartDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model=CartDetail
        fields='__all__'
class CartSerializers(serializers.ModelSerializer):
    cart_detail=CartDetailSerializers(source='detail_cart',many=True)
    class Meta:
        model=Cart
        fileds='__all__'
