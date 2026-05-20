from django.shortcuts import render, redirect


def index(request):

    if 'counter' not in request.session:
        request.session['counter'] = 0

    if 'visits' not in request.session:
        request.session['visits'] = 0

    request.session['counter'] += 1
    request.session['visits'] += 1

    context = {
        'counter': request.session['counter'],
        'visits': request.session['visits']
    }

    return render(request, 'index.html', context)


def destroy_session(request):

    request.session.flush()

    return redirect('/')


def add_two(request):

    request.session['counter'] += 2

    return redirect('/')


def increment(request):

    if request.method == 'POST':

        number = int(request.POST['number'])

        request.session['counter'] += number

    return redirect('/')