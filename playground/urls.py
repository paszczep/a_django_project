from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('hello/', views.say_hello),
    path('hello_world/', views.say_hello_world)
]