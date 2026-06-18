from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('created_user', views.created_user),
]