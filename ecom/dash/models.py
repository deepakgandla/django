from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

class Customer(models.Model):
    name=models.CharField(max_length=100,null=True)
    email=models.CharField(max_length=40,null=True)
    phone=models.CharField(max_length=10,null=True)
    owner=models.OneToOneField(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name
class Tag(models.Model):
    name=models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY=[
        ('indoor','indoor'),
        ('outdoor','outdoor')
    ]
    price=models.FloatField(null=True)
    name=models.CharField(max_length=90,null=True)
    category=models.CharField(max_length=100,null=True,choices=CATEGORY)
    description=models.CharField(max_length=10000,null=True,blank=True)
    tags=models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS=[
        ('out for deliver','out for deliver'),
        ('dispatched','dispatched'),
        ('delivered','delivered')
    ]

    customer=models.ForeignKey(Customer,null=True,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    ordered_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=100,null=True,choices=STATUS)

    def __str__(self):
        return self.product.name,self.customer.name
