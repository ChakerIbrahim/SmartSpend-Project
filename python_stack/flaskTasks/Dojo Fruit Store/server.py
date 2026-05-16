#!/usr/bin/env python3

from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("fruits.html")


@app.route("/checkout", methods=["POST"])
def checkout():
    strawberry = int(request.form["strawberry"])
    raspberry = int(request.form["raspberry"])
    blackberry = int(request.form["blackberry"])

    count = strawberry + raspberry + blackberry

    name = request.form["name"]
    student_id = request.form["student_id"]

    time = datetime.now().strftime("%B %d, %Y %I:%M %p")


    return render_template(
        "checkout.html",
        strawberry=strawberry,
        raspberry=raspberry,
        blackberry=blackberry,
        count=count,
        name=name,
        student_id=student_id,
        time=time
    )


if __name__ == "__main__":
    app.run(debug=True)