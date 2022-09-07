from django.contrib import admin
from django.urls import path, include
from superadmin import views

urlpatterns = [
    path('', views.index, name='index')
]