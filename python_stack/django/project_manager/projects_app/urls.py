from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register/', views.register),
    path('login/', views.login),
    path('dashboard/', views.dashboard),
    path('logout/', views.logout),

    path('projects/new/', views.new_project),
    path('projects/create/', views.create_project),
    path('projects/<int:id>/', views.project_details),
    path('projects/<int:id>/edit/', views.edit_project_page),
    path('projects/<int:id>/update/', views.update_project),
    path('projects/<int:id>/delete/', views.delete_project),

    path('projects/<int:id>/join/', views.join_project),
    path('projects/<int:id>/leave/', views.leave_project),
]