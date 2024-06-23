from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator

from retail.models import Product
# Create your models here.
class User(AbstractUser):
    profile_pic=models.ImageField(blank=True)
class Region(models.Model):
    abb_name=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
class City(models.Model):
    abb_name=models.CharField(max_length=3)
    name=models.CharField(max_length=100)
    region=models.ForeignKey(Region,on_delete=models.SET_NULL,null=True)
class Address(models.Model):
    street_address=models.TextField(blank=False,default="No adress has been provided")
    house_number=models.IntegerField(blank=False,default=0)
    locality=models.CharField(max_length=100)
    postal_code=models.IntegerField(blank=False)
    city=models.ForeignKey(City,on_delete=models.SET_NULL,null=True)
    client=models.ForeignKey(User,on_delete=models.CASCADE)
    resume=models.TextField(max_length=1000,blank=True)
class Status(models.Model):
    name=models.CharField(max_length=100)

class Opinion(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    client=models.ForeignKey(User,on_delete=models.CASCADE)
    rate=models.IntegerField(default=1,validators=[
        MaxValueValidator(5),
        MinValueValidator(0)
    ])
    comment=models.TextField()