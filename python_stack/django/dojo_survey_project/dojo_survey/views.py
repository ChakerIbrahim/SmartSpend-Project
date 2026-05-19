from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request, "index.html")

def results(request):
    name = request.POST["name"]
    location = request.POST["location"]
    fav_language = request.POST["fav-lang"]
    exp = request.POST["answer"]
    lang = request.POST.getlist("Lang")
    
    comment = request.POST["comments"]
    data = {"name" : name, "location" : location, "fav_language" : fav_language, "exp" : exp, "lang" : lang, "comment" : comment}
    return render(request, 'result.html',data)