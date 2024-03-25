import os,django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

import random
from products.models import Product,Brand
from faker import Faker

def seed_brand(n):
    fake=Faker()
    images=['1.jpeg','2.jpeg','3.jpeg','4.jpeg','5.jpeg','6.jpeg','7.jpeg','8.jpeg','9.jpeg','10.jpeg']
    for _ in range(n):
        Brand.objects.create(
            name=fake.name(),
            image=f'photo_brand/{images[random.randint(0,9)]}'

        )
def seed_product(n):
    fake=Faker()
    flag=['New','Sale','Feature']
    images=['1.jpeg','2.jpeg','3.jpeg','4.jpeg','5.jpeg','6.jpeg','7.jpeg','8.jpeg','9.jpeg','10.jpeg']
    brands=Brand.objects.all()
    for _ in range(n):
        Product.objects.create(
            name=fake.name(),
            flag=flag[random.randint(0,2)],
            price=round(random.uniform(20.99,99.9),2),
            image=f'photo_product/{images[random.randint(0,9)]}',
            sku=random.randint(100,10000000),
            subtitle=fake.text(max_nb_chars=400),
            descriptions=fake.text(max_nb_chars=40000),
            brand=brands[random.randint(0,len(brands)-1)],
            quantity=random.randint(5,100),
        )
#seed_brand(200)
seed_product(1500)
