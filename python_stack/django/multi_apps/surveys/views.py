from django.shortcuts import render ,HttpResponse,redirect

# Create your views here.
def display_survey(request):
    return HttpResponse("placeholder to display all the surveys created.")

def new_display(request):
    return HttpResponse("placeholder for users to add a new survey.")
