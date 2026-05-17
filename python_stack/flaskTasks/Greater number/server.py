from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "great_number_secret"


# Home route
@app.route("/")
def index():

    # Create random number only once
    if "number" not in session:
        session["number"] = random.randint(1, 100)

        # Store attempts count
        session["attempts"] = 0

        # Store game message
        session["message"] = ""

        # Store status (high, low, correct, lose)
        session["status"] = ""

    return render_template("index.html")


# Route to handle guessing form
@app.route("/guess", methods=["POST"])
def guess():

    # Get user guess from form
    user_guess = int(request.form["guess"])

    # Increase attempts
    session["attempts"] += 1

    # Check if guess is too high
    if user_guess > session["number"]:
        session["message"] = "Too High!"
        session["status"] = "high"

    # Check if guess is too low
    elif user_guess < session["number"]:
        session["message"] = "Too Low!"
        session["status"] = "low"

    # Correct guess
    else:
        session["message"] = f"Correct! You guessed it in {session['attempts']} attempts."
        session["status"] = "correct"

    # Lose after 5 attempts
    if session["attempts"] >= 5 and session["status"] != "correct":
        session["message"] = "You Lose! You used all 5 attempts."
        session["status"] = "lose"

    return redirect("/")


# Reset game session
@app.route("/reset")
def reset():

    # Clear all session data
    session.clear()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)