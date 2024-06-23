from django.urls import path
from .views import paying_page,buy,remove,process
urlpatterns=[
    path("",paying_page),
    path("buy",buy),
    path("process",process)
]