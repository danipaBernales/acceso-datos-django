from django.db import models
from django.conf import settings

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.name
class Brand(models.Model):
    name=models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.name
class ProductType(models.Model):
    name=models.CharField(max_length=100)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.category.name}:{self.name}"
class Warrant(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()

class Product(models.Model):
    sku=models.IntegerField(unique=True,blank=False,default=0)
    name=models.CharField(max_length=100,null=True)
    spects=models.TextField(blank=True)
    price=models.IntegerField(blank=False,default=0)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE,null=True)
    productType=models.ForeignKey(ProductType,on_delete=models.CASCADE,null=True)
    warrant=models.ManyToManyField(Warrant)
    def __str__(self) -> str:
        return self.name
class ProductImages(models.Model):
    title= models.CharField(max_length=100,null=True)
    img=models.ImageField()
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=False,default=0)