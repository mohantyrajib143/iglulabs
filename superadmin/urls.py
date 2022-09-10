from django.contrib import admin
from django.urls import path, include
from superadmin import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('employees_list/', views.employees_list, name='employees_list'),
    path('employees_grid/', views.employees_grid, name='employees_grid'),
]