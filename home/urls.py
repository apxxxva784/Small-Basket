from django.urls import path
from home import *
from home import views

urlpatterns = [
    path("", views.home, name="home"),
    path("products", views.products, name="products"),
]