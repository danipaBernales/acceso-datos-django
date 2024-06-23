from django import forms
from .models import User, Address

class userForm(forms.Form):
    first_name=forms.CharField(max_length=100,label="Nombre")
    last_name=forms.CharField(max_length=100,label="Apellido")
    email=forms.CharField(max_length=100,widget=forms.EmailInput(attrs={"placeholder":'Ingrese su correo'}))
    username=forms.CharField(max_length=100,label="Nombre Usuario")
    password=forms.CharField(max_length=100,label="contraseña",widget=forms.PasswordInput())

class AddressForm(forms.ModelForm):
    class Meta():
        model=Address
        exclude=["client"]
