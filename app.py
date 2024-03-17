# app.py
import sqlite3
from flask import Flask, render_template, request, flash, redirect, url_for

users = {
    'miguehm': '123abc',
    'admin': 'admin'
}

sueldo_base = 300

app = Flask(__name__)
app.secret_key = '123456abc' # usar una clave mas robusta como variable de entorno

@app.route('/login/')
def hello(color=None):
    return render_template('login.html', color=color)

@app.post('/login/')
def check_credentials():
    username = request.form['username']
    password = request.form['password']
    print(username, password)
    if username in users:
        if users[username] == password:
            print("ok")
            return redirect(url_for('index'))
        else:
            print("wrong")
    return redirect(url_for('hello'))

def get_db_connection():
    conn = sqlite3.connect('test.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    query = 'select *, ?+?*(0.3)*(AniosExpPrevia+(2024-AnioEntrada)) AS Salario from Trabajador'
    workers = conn.execute(query, (sueldo_base, sueldo_base)).fetchall()
    query = 'select AVG(?+?*(0.3)*(AniosExpPrevia+(2024-AnioEntrada))) AS SalarioPromedio from Trabajador'
    salario_promedio = conn.execute(query, (sueldo_base, sueldo_base)).fetchone()
    conn.close()
    return render_template('index.html', workers=workers, salario_promedio=salario_promedio['SalarioPromedio'])

@app.route('/add', methods=['POST'])
def add_post():
    title = request.form['title']
    content = request.form['content']
    conn = get_db_connection()
    conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)', (title, content))
    conn.commit()
    conn.close()
    flash('Post added successfully!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
