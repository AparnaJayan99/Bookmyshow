from django.urls import path
from .views import tickets, home, CreateUser

urlpatterns = [
    path("", home.as_view(), name="home"),
    path("check", tickets.as_view(), name="tickets"),
    path("add", CreateUser.as_view(), name="CreateUser"),
]