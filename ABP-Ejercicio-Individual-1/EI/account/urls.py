from django.urls import path
from account.views import *
from django.contrib.auth.views import LoginView
urlpatterns = [
    path('test/', test, name='test'),
    path('login/',LoginView.as_view(),name="login")
    # Include other view modules
]