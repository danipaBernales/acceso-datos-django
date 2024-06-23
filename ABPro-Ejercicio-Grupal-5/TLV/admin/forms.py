from retail.models import Product,ProductImages,ProductType,Category,Brand
from checkout.models import AnonymousOrder, AnonymousOrderDetail
from django import forms
class ProductForm(forms.ModelForm):
    class Meta():
        model=Product
        fields=["sku","name","spects","price","brand","productType"]
        labels={
            "sku":"SKU",
            "name":"Nombre del producto",
            "spects":"Especificaciones del producto",
            "brand":"Marca",
            "price":"Precio",
            "productType":"Tipo de producto"
        }
class ProductImageForm(forms.ModelForm):
    class Meta():
        model=ProductImages
        fields='__all__'
class ProductTypeForm(forms.ModelForm):
    class Meta():
        model=ProductType
        fields='__all__'
class CategoryForm(forms.ModelForm):
    class Meta():
        model=Category
        fields='__all__'
class BrandForm(forms.ModelForm):
    class Meta:
        model=Brand
        fields='__all__'
    
class AnonymousOrderForm(forms.ModelForm):
    class Meta:
        model=AnonymousOrder
        exclude=["estimated_arrival","status","purchase_day","seller"]
        fields="__all__"

class AnonymousOrderDetailForm(forms.ModelForm):
    class Meta:
        model=AnonymousOrderDetail
        fields="__all__"
