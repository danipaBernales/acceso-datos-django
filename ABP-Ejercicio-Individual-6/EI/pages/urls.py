from django.urls import path
from pages.views import welcome,home
urlpatterns = [
    path("",welcome,name="Bienvenida"),
    path("home",home,name="home"),
    # Include other view modules
]