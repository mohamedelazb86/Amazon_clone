from django.db import models
from django.contrib.auth.models import User
from utils.generate_code import generate_code
from django.utils import timezone
from products.models import Product
from accounts.models import Address
import datetime

ORDER_STATUS=[
    ('Recieved','Recieved'),
    ('Processed','Processed'),
    ('Shipped','Shipped'),
    ('Delivered','Delivered'),
    ]
class Order(models.Model):
    user=models.ForeignKey(User,related_name='order_user',on_delete=models.SET_NULL,null=True,blank=True)
    status=models.CharField(max_length=50,choices=ORDER_STATUS)
    code=models.CharField(max_length=25,default=generate_code)
    order_time=models.DateTimeField(default=timezone.now)
    delivery_time=models.DateTimeField(null=True,blank=True)
    delivery_address=models.ForeignKey(Address,related_name='order_address',on_delete=models.SET_NULL,null=True,blank=True)
    copoun=models.ForeignKey('Copoun',related_name='order_copoun',on_delete=models.SET_NULL,null=True,blank=True)
    total=models.FloatField(null=True,blank=True)
    total_with_copoun=models.FloatField(null=True,blank=True)

    


class OrderDetail(models.Model):
    order=models.ForeignKey(Order,related_name='detail_order',on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,blank=True,related_name='detail_product')
    price=models.FloatField()
    quantity=models.IntegerField()
    total=models.FloatField(null=True,blank=True)

    def __str__(self):
        return str(self.order)
    


CART_STATUS=[
    ('Completed','Completed'),
    ('Inprogress','Inprogress'),
]

class Cart(models.Model):
    user=models.ForeignKey(User,related_name='cart_user',on_delete=models.SET_NULL,null=True,blank=True)
    status=models.CharField(max_length=50,choices=CART_STATUS)
    
    copoun=models.ForeignKey('Copoun',related_name='cart_copoun',on_delete=models.SET_NULL,null=True,blank=True)
    
    total_with_copoun=models.FloatField(null=True,blank=True)

    @property
    def cart_total(self):
        total=0
        for item in self.detail_cart.all():
            total += item.total
        return total

    


class CartDetail(models.Model):
    cart=models.ForeignKey(Cart,related_name='detail_cart',on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,blank=True,related_name='cart_product')
    quantity=models.IntegerField(default=1)
    total=models.FloatField(null=True,blank=True)

   
    
class Copoun(models.Model):
    code=models.CharField(max_length=50)
    start_date=models.DateField(default=timezone.now)
    end_date=models.DateField(null=True,blank=True)
    quantity=models.IntegerField()
    discount=models.FloatField()

       

    
    
    def save(self,*args,**kwargs):
        week=datetime.timedelta(days=7)
        self.end_date=self.start_date+week
        super(Copoun,self).save(*args,**kwargs)



    