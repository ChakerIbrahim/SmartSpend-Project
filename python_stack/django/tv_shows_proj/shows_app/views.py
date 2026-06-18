from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages

# READ ALL SHOWS
def index(request):
    context = {
        "all_shows":Show.objects.all()
    }
    return render(request,"index.html",context)

# SHOW CREATE FORM
def new(request):
    return render(request,"new.html")

# CREATE new row in database
def create(request):
    show =Show.objects.create(
        title = request.POST['title'],
        network = request.POST['network'],
        release_date = request.POST['release_date'],
        desc = request.POST['desc']
    )
    return redirect(f"/shows/{show.id}/")

# READ ONE SHOW
def show(request,id):
    context = {
        "show":Show.objects.get(id = id)
    }
    return render(request,"show.html",context)

# SHOW EDIT FORM
def edit(request,id):
    context = {
        "show":Show.objects.get(id = id)
    }
    return render(request,"edit.html",context)

# UPDATE SHOW
def update(request,id):
    errors = Show.objects.show_validator(request.POST ,id = id)
    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request,value)
    else: 
    # If no errors, update data      
        show = Show.objects.get(id = id)
    # UPDATE fields
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = request.POST['release_date']
        show.desc = request.POST['desc']
    # SAVE CHANGES
        show.save()
    return redirect(f"/shows/{show.id}/")
# DELETE SHOW
def destroy(request,id):
    show = Show.objects.get(id = id)
    show.delete()
    return redirect('/shows/')