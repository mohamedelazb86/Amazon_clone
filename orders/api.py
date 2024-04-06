from .serializers import OrderDetailserializers,OrderSerializers
from .serializers import CartDetailSerializers,CartSerializers
from .models import Order,OrderDetail,Copoun,Cart,CartDetail
from django.contrib.auth.models import User
from rest_framework import generics
from django.shortcuts import get_object_or_404
import datetime
from settings.models import Delivery_fee
from rest_framework.response import Response
from rest_framework import status
from accounts.models import Address
from products.models import Product


class OrderApi(generics.ListAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderSerializers

    def get_queryset(self):
        queryset = super(OrderApi, self).get_queryset()
        user=User.objects.get(username=self.kwargs['username'])
        queryset = queryset.filter(user=user)
        return queryset
class OrderDetailApi(generics.RetrieveAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderSerializers


class Apply_Copoun(generics.GenericAPIView):
    def post(self,request,*args,**kwargs):
        user=User.objects.get(username=self.kwargs['username'])    # from url
        code=request.data['copoun_code']
        cart=Cart.objects.get(user=user,status='Inprogress')
        #cart_detail=CartDetail.objects.filter(cart=cart)
        #copoun=Copoun.objects.get(code=code)
        copoun=get_object_or_404(Copoun,code=code)
        delivery_fee=Delivery_fee.objects.last().fee
        if copoun and copoun.quantity > 0 :
            mydate=datetime.datetime.today().date()
            if mydate >= copoun.start_date and mydate <= copoun.end_date:
                copoun_value=round(cart.cart_total / 100 * copoun.discount,2)
                subtotal=cart.cart_total+delivery_fee
                total=subtotal+copoun_value

                cart.copoun=copoun
                cart.total_with_copoun=total

                cart.save()
                copoun.quantity -=1
                copoun.save()

                return Response({'message':'ok copoun done '},status=status.HTTP_200_OK)
            
class CreatOrderApi(generics.GenericAPIView):
    # cart --------- order      cart_detail ----------- order_detatil
    def post(self,request,*args,**kwargs):
        user=User.objects.get(username=self.kwargs['username'])  # from url
        code=request.data['payment_code']
        address=request.data['address_id']
        cart,created=Cart.objects.get_or_create(user=user,status='Inprogress')
        cart_detail=CartDetail.objects.get(cart=cart)
        delivery_address=Address.objects.get(id=address)
        new_order=Order.objects.create(
            user=user,
            status='Recieved',
            delivery_address=delivery_address,
            copoun=cart.copoun,
            total=cart.cart_total,
            total_with_copoun=cart.total_with_copoun
            
        )
        for item in cart_detail:
            product=Product.objects.get(id=item.product.id)
            Order.objects.create(
                order=new_order,
                product=product,
                quantity=item.quantity,
                price=item.product.price,
                total=round(item.quantity * item.product.price,2)
                

            )
            product.quantity -=1
            product.save()
        cart.status='Completed'
        cart.save()    


        # send email


class Create_update_delete_Cart():
    pass

            




