from django.db import models
from django.contrib.auth.models import User

# Create your models here.
ADDRESS_TYPE=[
    ('Home','Home'),
    ('Office','Office'),
    ('Others','Others'),
    ]
class Address(models.Model):
    user=models.ForeignKey(User,related_name='address_user',on_delete=models.CASCADE)
    address=models.CharField(max_length=150)
    address_type=models.CharField(max_length=50,choices=ADDRESS_TYPE)

    def __str__(self):
        return str(self.user)
    
    
