from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/login/')
@app.route('/login/<color>')
def hello(color=None):
    return render_template('login.html', color=color)
