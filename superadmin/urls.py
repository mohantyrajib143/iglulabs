from django.contrib import admin
from django.urls import path, include
from superadmin import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),

    # departments urls starts here
    path('departments/', views.departments, name='departments'),
    path('update_departments_status/<int:id>', views.update_departments_status, name='update_departments_status'),
    path('update_departments/<int:id>', views.update_departments, name='update_departments'),
    path('delete_departments/<int:id>', views.delete_departments, name='delete_departments'),

    # designation urls starts here
    path('designations/', views.designations, name='designations'),
    path('update_designation_status/<int:id>', views.update_designation_status, name='update_designation_status'),
    path('update_designation/<int:id>', views.update_designation, name='update_designation'),
    path('delete_designation/<int:id>', views.delete_designation, name='delete_designation'),

    # employees urls starts here
    path('employees_list/', views.employees_list, name='employees_list'),
    path('employees_grid/', views.employees_grid, name='employees_grid'),
]