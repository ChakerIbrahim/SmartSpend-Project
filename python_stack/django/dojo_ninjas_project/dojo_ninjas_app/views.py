from django.shortcuts import render, redirect
from .models import Dojo, Ninja


# Display page with all dojos and ninjas
def index(request):

    context = {
        "all_dojos": Dojo.objects.all()
    }

    return render(request, "index.html", context)


# Create a new dojo
def create_dojo(request):

    Dojo.objects.create(
        name=request.POST["name"],
        city=request.POST["city"],
        state=request.POST["state"]
    )

    return redirect("/")


# Create a new ninja
def create_ninja(request):

    # Get selected dojo from dropdown
    dojo = Dojo.objects.get(id=request.POST["dojo_id"])

    Ninja.objects.create(
        first_name=request.POST["first_name"],
        last_name=request.POST["last_name"],
        dojo=dojo
    )

    return redirect("/")


# Delete dojo and all related ninjas
def delete_dojo(request, dojo_id):

    dojo = Dojo.objects.get(id=dojo_id)

    dojo.delete()

    return redirect("/")