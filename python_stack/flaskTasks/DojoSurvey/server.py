from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def display_main():
    return render_template("index.html")


@app.route("/result", methods =["POST"])
def display_info():
    name = request.form["name"]
    location = request.form["location"]
    language = request.form["language"]
    comment = request.form["comment"]
    return render_template(
        "result.html", name=name, location=location, language=language, comment=comment
    )


if __name__ == "__main__":
    app.run(debug=True)
