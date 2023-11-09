from django.urls import path
from superadmin import views

urlpatterns = [
    path('', views.mylogin, name='mylogin'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('projects/', views.projects, name='projects'),
]