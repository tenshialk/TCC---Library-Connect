from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def capa():
    return render_template('capa.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/biblioteca')
def biblioteca():
    return render_template('biblioteca.html')

@app.route('/perfil')
def perfil():
    return render_template('perfil.html')

@app.route('/livro')
def livro():
    return render_template('livro.html')

@app.route('/geral')
def geral():
    return render_template('geral.html')