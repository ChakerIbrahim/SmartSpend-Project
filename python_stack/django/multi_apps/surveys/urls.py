from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_survey),
    path('new',views.new_display)
]