from django.urls import path 
from . import views
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('forgot-password/', views.forgot_password_view, name='forgot_password'),
    path('reset-password/', views.reset_password_view, name='reset_password'),
    path('verify-email/', views.verify_email_view, name='verify_email'),
    path('success/', views.success_view, name='success'),
]