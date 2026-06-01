from django.shortcuts import render, redirect
from .models import Dojo, Ninja


# Display all dojos and their ninjas
def index(request):

    context = {
        "all_dojos": Dojo.objects.all()
    }

    return render(request, "index.html", context)


# Process dojo creation form
def create_dojo(request):

    # Call model manager method
    Dojo.objects.create_dojo(request.POST)

    return redirect("/")


# Process ninja creation form
def create_ninja(request):

    # Call model manager method
    Ninja.objects.create_ninja(request.POST)

    return redirect("/")


# BONUS: Delete a dojo and all associated ninjas
def delete_dojo(request, dojo_id):

    dojo = Dojo.objects.get(id=dojo_id)

    dojo.delete()

    return redirect("/")