from django.urls import path
from superadmin import views

urlpatterns = [
    path('', views.mylogin, name='mylogin'),
    path('logout/', views.mylogout, name="mylogout"),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('projects/', views.projects, name='projects'),
    path('updateProjectStatus/<int:id>/', views.updateProjectStatus, name='updateProjectStatus'),
    path('projects/', views.projects, name='projects'),
    path('editProjects/<int:id>/', views.editProjects, name='editProjects'),
    path('deleteProjects/<int:id>/', views.deleteProjects, name='deleteProjects'),
]