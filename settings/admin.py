from django.contrib import admin
from .models import Settings

class SettingAdmin(admin.ModelAdmin):
    list_display=['name','call_us']
    
    search_fields=['name','subtitle']


admin.site.register(Settings)

