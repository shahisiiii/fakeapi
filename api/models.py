from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Products(models.Model):
    product_name=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to="product_image")
    


class Reviews(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Products,on_delete=models.CASCADE) 
    review=models.CharField(max_length=100)
    rating=models.PositiveIntegerField()

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Products,on_delete=models.CASCADE) 
    count=models.PositiveIntegerField(default=1)
    options=(
        ('in-cart','in-cart'),
        ('order-placed','order-placed'),
        ('cancelled','cancelled')
    )
    
    status=models.CharField(max_length=100,choices=options,default='in-cart')