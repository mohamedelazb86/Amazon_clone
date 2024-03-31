from django.db import models

class Settings(models.Model):
    name=models.CharField(max_length=120)
    logo=models.ImageField(upload_to='logo')
    subtitle=models.TextField(max_length=1000)
    call_us=models.CharField(max_length=50)
    email_us=models.CharField(max_length=50)
    phones=models.TextField(max_length=100)
    address=models.TextField(max_length=100)
    andriod_app=models.URLField(null=True,blank=True)
    ios_app=models.URLField(null=True,blank=True)
    facebook=models.URLField(null=True,blank=True)
    youtube=models.URLField(null=True,blank=True)

    def __str__(self):
        return self.name
    

class Delivery_fee(models.Model):
    fee=models.IntegerField()

    def __Str__(self):
        return str(self.fee)