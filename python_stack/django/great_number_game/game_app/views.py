import random
from django.shortcuts import render, redirect

# Display the main game page
def index(request):

    # Check if random number already exists in session
    if 'number' not in request.session:

        # Save random number between 1 and 100
        request.session['number'] = random.randint(1, 100)

        # Store message for user
        request.session['message'] = ''

        # Store color for result box
        request.session['color'] = ''

        # Count user attempts
        request.session['attempts'] = 0

        # Check if game finished
        request.session['game_over'] = False

    # Render HTML page
    return render(request, 'index.html')


# Process user's guess
def guess(request):

    # Check if request method is POST
    if request.method == 'POST':

        # Get user guess from form
        user_guess = int(request.POST['guess'])

        # Increase attempts count
        request.session['attempts'] += 1

        # Check if guess is correct
        if user_guess == request.session['number']:

            # Success message
            request.session['message'] = f"{request.session['number']} was the number!"

            # Green color for success
            request.session['color'] = 'green'

            # End game
            request.session['game_over'] = True

        # Check if attempts reached 5
        elif request.session['attempts'] >= 5:

            # Lose message
            request.session['message'] = f"You Lose! The number was {request.session['number']}"

            # Red color
            request.session['color'] = 'red'

            # End game
            request.session['game_over'] = True

        # If guess is too low
        elif user_guess < request.session['number']:

            # Display too low message
            request.session['message'] = "Too Low!"

            # Red color
            request.session['color'] = 'red'

        # If guess is too high
        else:

            # Display too high message
            request.session['message'] = "Too High!"

            # Red color
            request.session['color'] = 'red'

    # Redirect back to home page
    return redirect('/')


# Reset game
def reset(request):

    # Clear all session data
    request.session.flush()

    # Redirect to home page
    return redirect('/')