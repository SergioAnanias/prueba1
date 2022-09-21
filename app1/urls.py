from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index),
    path('userinfo', views.userinfo),
    path('toys', views.toys),
    path('clothes', views.clothes)
]