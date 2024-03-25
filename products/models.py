from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
FLAG_TYPE=[
    ('New','New'),
    ('Sale','Sale'),
    ('Feature','Feature'),
    ]
class Product(models.Model):
    name=models.CharField(max_length=120,verbose_name=_('name'))
    flag=models.CharField(_('flag'),max_length=50,choices=FLAG_TYPE)
    price=models.FloatField(_('price'))
    image=models.ImageField(upload_to='photo_product',verbose_name=_('image'))
    sku=models.IntegerField(_('sku'))
    subtitle=models.TextField(_('subtitle'),max_length=500)
    descriptions=models.TextField(_('descriptions'),max_length=50000)
    brand=models.ForeignKey('Brand',related_name='product_brand',on_delete=models.SET_NULL,null=True,blank=True)
    tags = TaggableManager()
    slug=models.SlugField(_('slug'),null=True,blank=True)
    quantity=models.IntegerField(_('quantity'))


    def __str__(self):
        return self.name
    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super(Product,self).save(*args,**kwargs)

class Product_Image(models.Model):
    product=models.ForeignKey(Product,related_name='image_product',on_delete=models.CASCADE)
    image=models.ImageField(upload_to='photos')

    def __str__(self):
        return str(self.product)
    
class Brand(models.Model):
    name=models.CharField(max_length=120)
    image=models.ImageField(upload_to='photo_brand')
    slug=models.SlugField(null=True,blank=True)

    def __str__(self):
        return self.name
    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super(Brand,self).save(*args,**kwargs)

    
class Review(models.Model):
    product=models.ForeignKey(Product,related_name='review_product',on_delete=models.CASCADE)
    user=models.ForeignKey(User,related_name='review_user',on_delete=models.SET_NULL,null=True,blank=True)
    review=models.TextField(max_length=1000)
    rate=models.IntegerField(choices=[(i,i) for i in range(1,6)])
    publish_date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.product}--{self.user}'


    

