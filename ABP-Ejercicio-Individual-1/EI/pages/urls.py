from django.urls import path
from pages.views import welcome,home,logout
urlpatterns = [
    path("",welcome,name="Bienvenida"),
    path("home",home,name="home"),
    path("logout",logout,name="logout")
    # Include other view modules
]