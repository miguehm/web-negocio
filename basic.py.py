from flask import Flask
from markupsafe import escape

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return f"<p>{escape(2+2)}, World!</p>"

@app.route("/secret")
def our_secret():
    return f"<p>You got me!</p>"

@app.route("/user/<username>")
def show_user_profile(username):
    return f"<p>You are {escape(username)}</p>"

@app.route("/num/<int:number>")
def get_factorial(number):
    return f"<p>Factorial of {escape(number)} is {factorial(number)}</p>"

if __name__ == "__main__":
    app.run()
