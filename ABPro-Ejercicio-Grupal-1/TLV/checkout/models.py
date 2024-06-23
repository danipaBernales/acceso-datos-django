from django.db import models
from django.utils.timezone import now
from datetime import timedelta
from retail.models import Product
from account.models import User
# Create your models here.
class Status(models.Model):
    name=models.CharField(max_length=100,null=True)
    def __str__(self) -> str:
        return self.name
class PayingMethod(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name   
class Shopping(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    client=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    quantity=models.IntegerField(blank=False,default=1)
    class Meta:
        unique_together=["product","client"]
class Checkout(models.Model):
    client=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    purchase_day=models.DateTimeField(blank=False,default=now)
    estimated_arrival=models.DateField(blank=False,default=now()+timedelta(days=14))
    paying_method=models.ForeignKey(PayingMethod,on_delete=models.SET_NULL,null=True)
    status=models.ForeignKey(Status,on_delete=models.SET_NULL,null=True)
class CheckoutDetail(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField(blank=False,default=1)
    checkout=models.ForeignKey(Checkout,on_delete=models.CASCADE)

class AnonymousOrder(models.Model):
    username=models.CharField(max_length=100)
    purchase_day=models.DateTimeField(blank=False,default=now)
    estimated_arrival=models.DateField(blank=False,default=now()+timedelta(days=14))
    paying_method=models.ForeignKey(PayingMethod,on_delete=models.SET_NULL,null=True)
    status=models.ForeignKey(Status,on_delete=models.SET_NULL,null=True)
    address=models.CharField(max_length=1000)
    seller=models.ForeignKey(User,on_delete=models.CASCADE)

class AnonymousOrderDetail(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField(blank=False,default=1)
    anonymousorder=models.ForeignKey(AnonymousOrder,on_delete=models.CASCADE)