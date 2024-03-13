# app.py
import sqlite3
from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = '123456abc' # usar una clave mas robusta como variable de entorno

def get_db_connection():
    conn = sqlite3.connect('test.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)

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
