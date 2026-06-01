from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('tasks/new/', views.new),
    path('tasks/create/', views.create),
    path('tasks/<int:id>/', views.show),
    path('tasks/<int:id>/edit/', views.edit),
    path('tasks/<int:id>/update/', views.update),
    path('tasks/<int:id>/delete/', views.delete),
    
]
