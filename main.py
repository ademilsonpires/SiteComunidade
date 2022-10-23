from flask import Flask, render_template, url_for
from forms import FormLogin, FormCriarConta


app = Flask(__name__)

app.config['SECRET_KEY'] = '9e57ca58a84f6cd3b02b2114fd90ef7c'

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/contato')
def contato():
    return render_template('contato.html')


@app.route('/listagem-usuarios')
def usuarios():
    lista_usuarios = {'Ademilson', 'Abrão','Cassyo'}
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)

@app.route('/login')
def login():
    form_login = FormLogin()
    form_criarconta = FormCriarConta()
    return render_template('login.html', form_login=form_login, form_criarconta=form_criarconta)

if __name__ == '__main__':
    app.run(debug=True)