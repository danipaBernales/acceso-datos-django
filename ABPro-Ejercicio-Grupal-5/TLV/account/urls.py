from django.urls import path
from django.contrib.auth.views import LoginView
from .views import logout_view,signup,profile,add_direction
urlpatterns=[
    path('login',LoginView.as_view(),name="login"),
    path("logout",logout_view,name="logout"),
    path("signup",signup),
    path("profile",profile),
    path("add_direction",add_direction)
]
