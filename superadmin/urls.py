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

    # holidays urls starts here
    path('holidays/', views.holidays, name='holidays'),
    path('update_holidays_status/<int:id>', views.update_holidays_status, name='update_holidays_status'),
    path('update_holidays/<int:id>', views.update_holidays, name='update_holidays'),
    path('delete_holidays/<int:id>', views.delete_holidays, name='delete_holidays'),

    # assets urls starts here
    path('assets/', views.assets, name='assets'),
    path('update_assets_status/<int:id>', views.update_assets_status, name='update_assets_status'),
    path('update_assets/<int:id>', views.update_assets, name='update_assets'),
    path('delete_assets/<int:id>', views.delete_assets, name='delete_assets'),

    # employees urls starts here
    path('employees_list/', views.employees_list, name='employees_list'),
    
    path('employees_grid/', views.employees_grid, name='employees_grid'),
    path('employees_profile/', views.employees_profile, name='employees_profile'),
    path('add_family_info/', views.add_family_info, name='add_family_info'),
    path('delete_emp_family_data/<int:id>', views.delete_emp_family_data, name='delete_emp_family_data'),
]