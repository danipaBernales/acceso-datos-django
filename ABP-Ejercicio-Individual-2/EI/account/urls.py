from django.urls import path
from account.views import test,logout_view
from django.contrib.auth.views import LoginView
urlpatterns = [
    path('test/', test, name='test'),
    path('login/',LoginView.as_view(),name="login"),
    path("logout",logout_view,name="logout")
    # Include other view modules
]