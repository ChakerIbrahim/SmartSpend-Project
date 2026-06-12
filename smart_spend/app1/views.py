from django.shortcuts import render

def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    return render(request, 'register.html')

def forgot_password_view(request):
    return render(request, 'forgot_password.html')

def reset_password_view(request):
    return render(request, 'reset_password.html')

def verify_email_view(request):
    return render(request, 'verify_email.html')

def success_view(request):
    return render(request, 'success.html')