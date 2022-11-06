from flask import render_template,request,  redirect, url_for, flash
from comunidadeblogdopython import app, database, bcrypt
from comunidadeblogdopython.forms import FormLogin, FormCriarConta
from comunidadeblogdopython.models import Usuario

lista_usuarios = {'Ademilson', 'Elayne', 'Kerolayne'}  # lista de teste


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/contato')
def contato():
    return render_template('contato.html')


@app.route('/listagem-usuarios')
def usuarios():
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
        senha_cript = bcrypt.generate_password_hash(form_criarconta.senha.data)
        usuario = Usuario(username=form_criarconta.username.data, email=form_criarconta.email.data, senha=senha_cript)
        database.session.add(usuario)
        database.session.commit()
        # adicionar a sessão
        #commit da sessao

        flash(f'Conta criada com sucesso para o email: {form_criarconta.email.data}', 'alert-success')
        return redirect(url_for('home'))
    return render_template('login.html', form_login=form_login, form_criarconta=form_criarconta)
