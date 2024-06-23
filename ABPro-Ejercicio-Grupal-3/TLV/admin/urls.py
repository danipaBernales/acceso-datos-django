from django.urls import path
from .views import admin_view,take_order,submit_order
urlpatterns=[
    path("",admin_view),
    path("takeOrder",take_order),
    path("submitOrder",submit_order)
   
]