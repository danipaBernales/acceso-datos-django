from django import forms
from .models import User
class RegisterForm(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(max_length=100,widget=forms.PasswordInput)

class userForm(forms.Form):
    first_name=forms.CharField(max_length=100,label="Nombre")
    last_name=forms.CharField(max_length=100,label="Apellido")
    email=forms.CharField(max_length=100,widget=forms.EmailInput(attrs={"placeholder":'Ingrese su correo'}))
    username=forms.CharField(max_length=100)
    password=forms.CharField(max_length=100,widget=forms.PasswordInput())
class UserModelForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password"]