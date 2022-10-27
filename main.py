from flask import Flask, render_template, url_for, request, flash, redirect
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
    lista_usuarios = {'Ademilson', 'Elayne','Kerolayne'} #lista de teste
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)

@app.route('/login',methods=['GET','POST'])
def login():
    form_login = FormLogin()
    form_criarconta = FormCriarConta()
    if form_login.validate_on_submit() and 'botao_submit_login' in request.form:
        # fez login com sucesso
        flash(f'Login feito com sucesso: {form_login.email.data}','alert-success')
        return redirect(url_for('home'))
    if form_criarconta.validate_on_submit() and 'botao_submit_criar_conta' in request.form:
        # criar conta com sucesso
        flash(f'Conta criada com sucesso para o email: {form_criarconta.email.data}', 'alert-success')
        return redirect(url_for('home'))
    return render_template('login.html', form_login=form_login, form_criarconta=form_criarconta)
if __name__ == '__main__':
    app.run(debug=True)