from django.shortcuts import render
from .models import Order,Cart,CartDetail,Copoun
from settings.models import Delivery_fee
from django.shortcuts import get_object_or_404
import datetime

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
    delivery_fee=Delivery_fee.objects.last().fee
    

    if request.method == 'POST':
        #copoun=Copoun.objects.get(code=request['copoun_code'])
        copoun=get_object_or_404(Copoun,code=request.POST['copoun_code'])
        if copoun and copoun.quantity > 0 :
            mydate=datetime.datetime.today().date()
            if mydate >= copoun.start_date and mydate <= copoun.end_date:
                copoun_value=round(cart.cart_total / 100 * copoun.discount,2)
                subtotal=cart.cart_total
                discount=copoun_value
                total=round(subtotal+delivery_fee-discount,2)

                cart.copoun=copoun
                cart.total_with_copoun=total

                copoun.quantity -=1
                copoun.save()

                context = {
                    'cart':cart,
                    'cart_detail':cart_detail,
                    'subtotal':subtotal,
                    'delivery_fee':delivery_fee,
                    'discount':discount,
                    'total':total


                }

                return render(request,'orders/checkout.html',context)
                
            





    subtotal=cart.cart_total
    
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
