from django.urls import path
from superadmin import views

urlpatterns = [
    path('', views.index, name='index'),
]