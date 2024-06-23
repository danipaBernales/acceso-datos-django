from django.urls import path
from .views import paying_page,buy,remove,process,order_detail
urlpatterns=[
    path("",paying_page),
    path("buy",buy),
    path("process",process),
    path("detail/<int:id>",order_detail)
]