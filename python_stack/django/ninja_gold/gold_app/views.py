from django.shortcuts import render, redirect
from random import randint
# Create your views here.
def index(request):
    if 'total_number_of_gold' not in request.session:
        request.session['total_number_of_gold'] = 0
 
 
    return render (request,'index.html')
 
def process_money(request):
    if request.method == 'POST':
        if request.POST['location'] == 'farm':
            gold =randint(10,20)
        elif request.POST['location'] == 'cave':
            gold =randint(5,10)
        elif request.POST['location'] == 'house':
            gold =randint(1,10)
        elif request.POST['location'] == 'quest':
            gold =randint(-50,50)
        # gold =randint(int(request.POST['min']),int(request.POST['max']))
        request.session['total_number_of_gold'] += gold
        
    return redirect('/')