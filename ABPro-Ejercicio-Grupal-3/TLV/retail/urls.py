from django.urls import path
from .views import home,shopping_cart
urlpatterns=[
    path("",home),
    path("shopping-cart",shopping_cart)
]