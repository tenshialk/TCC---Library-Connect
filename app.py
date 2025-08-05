from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def capa():
    return render_template('capa.html')

@app.route('/login')
def login():
    return render_template('login.html')