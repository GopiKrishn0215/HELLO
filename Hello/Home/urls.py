
from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path("",views.index, name='home'),
    path("about",views.about, name='About'),
    path("services", views.services, name='services')
    
]
