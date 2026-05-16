from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "welcome to our project"

@app.route('/home/<name>')
def welcome(name):
    return "welcome home MR."+ name 

@app.route('/sum/<int:num1>/<int:num2>')
def sum(num1,num2):
    return f"{num1} + {num2} = {num1+num2}"

if __name__ == "__main__":
    app.run(debug=True)
    