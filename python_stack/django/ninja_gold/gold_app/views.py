from django.shortcuts import render ,redirect
from random import random 

# Create your views here.
def index(request):
    return render(request, 'index.html')

def money(request):
    gold = random.randint(10,20)
    request.session['gold'] += gold
    return redirect('/')  