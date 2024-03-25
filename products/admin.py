from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Product,Product_Image,Review,Brand

class ProImage(admin.TabularInline):
    model=Product_Image


class ProductAdmin(SummernoteModelAdmin):
    list_display=['name','flag','sku']
    list_filter=['flag','brand']
    search_fields=['name','subtitle']

    summernote_fields = ('subtitle','descriptions')
    inlines=[ProImage]



#admin.site.register(Product_Image)
admin.site.register(Product,ProductAdmin)
admin.site.register(Review)
admin.site.register(Brand)
