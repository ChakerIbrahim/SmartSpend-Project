from django.shortcuts import render, redirect
from .models import User
 
# Create your views here.
 
# Shows the home page with all users listed
def index(request):
    context = {
        "all_users": User.objects.all()  # Fetch all users from the database
    }
    return render(request, "index.html", context)
 
# Handles the form submission to create a new user
def created_user(request):
    User.objects.create(
        first_name = request.POST['first_name'],  # Get first name from form
        last_name = request.POST['last_name'],    # Get last name from form
        email = request.POST['email'],            # Get email from form
        age = request.POST['age']                 # Get age from form
    )
    return redirect('/')  # Redirect back to home page after saving