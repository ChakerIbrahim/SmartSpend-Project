from flask import Flask ,render_template,request
app = Flask(__name__)
@app.route('/')
def display_main():
    return render_template('index.html')

@app.route('/result',method = ['POST'])
def display_info():
    name_from_form = request.form['name']
    location_from_form = request.form['location']
    language_from_form = request.form['language']
    comment_from_form = request.form['comment']
    return render_template(
        "result.html",
        user = name_from_form,
        place = location_from_form,
        lang = language_from_form,
        sms = comment_from_form
    )

if __name__ == "__main__":
    app.run(debug=True)