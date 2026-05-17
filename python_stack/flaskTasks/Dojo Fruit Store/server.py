# # import Flask tools

from flask import Flask, render_template, request

# import datetime to show current time

from datetime import datetime

# create Flask app

app = Flask(__name__)

# home page route

@app.route("/")
def index():
    return render_template("fruits.html")

# checkout route
# methods POST because form sends data using POST

@app.route("/checkout", methods=["POST"])
def checkout():

    # get fruit quantities from form
    # convert string to integer
    
    strawberry = int(request.form["strawberry"])
    raspberry = int(request.form["raspberry"])
    blackberry = int(request.form["blackberry"])
    
    # calculate total fruits
    
    count = strawberry + raspberry + blackberry
    
    # get user information
    
    name = request.form["name"]
    student_id = request.form["student_id"]
    
    # get current date and time
    
    time = datetime.now().strftime("%B %d, %Y %I:%M %p")

    # send data to checkout page
    
    return render_template(
        "checkout.html",
        strawberry=strawberry,
        raspberry=raspberry,
        blackberry=blackberry,
        count=count,
        name=name,
        student_id=student_id,
        time=time,
    )

# run Flask server

if __name__ == "__main__":
    app.run(debug=True)
