from django.shortcuts import render
from .models import Order,Cart,CartDetail
from settings.models import Delivery_fee

from accounts.models import Address


def order_list(request):
    orders=Order.objects.filter(user=request.user)
    
    context={
        'orders':orders,
        
    }
    return render(request,'orders/orderlist.html',context)

def checkout(request):

    cart=Cart.objects.get(user=request.user,status='Inprogress')
    cart_detail=CartDetail.objects.filter(cart=cart)
    subtotal=cart.cart_total
    delivery_fee=Delivery_fee.objects.last().fee
    discount=0
    total=subtotal+delivery_fee


    context={
        'cart':cart,
        'cart_detail':cart_detail,
        'subtotal':subtotal,
        'delivery_fee':delivery_fee,
        'discount':discount,
        'total':total

        
    }


    return render(request,'orders/checkout.html',context)
