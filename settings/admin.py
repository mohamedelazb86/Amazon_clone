from django.contrib import admin
from .models import Settings,Delivery_fee

class SettingAdmin(admin.ModelAdmin):
    list_display=['name','call_us']
    
    search_fields=['name','subtitle']


admin.site.register(Settings)
admin.site.register(Delivery_fee)

