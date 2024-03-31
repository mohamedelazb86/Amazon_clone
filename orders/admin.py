from django.contrib import admin

from .models import Order,OrderDetail,CartDetail,Cart,Copoun
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(CartDetail)
admin.site.register(Copoun)
