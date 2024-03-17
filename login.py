from flask import Flask, request, render_template, flash, url_for, redirect

users = {
    'miguehm': '123abc',
    'admin': 'admin'
}

app = Flask(__name__)
app.secret_key = '123456abc' # usar una clave mas robusta como variable de entorno

@app.route('/login/')
def hello(color=None):
    return render_template('login.html', color=color)

@app.post('/login/')
def check_credentials():
    username = request.form['username']
    password = request.form['password']
    if users[username] == password:
        print("ok")
        return render_template('index.html')
    else:
        print("wrong")
