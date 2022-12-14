from flask import render_template,request,  redirect, url_for, flash
from comunidadeblogdopython import app, database, bcrypt
from comunidadeblogdopython.forms import FormLogin, FormCriarConta, FormEditarPerfil
from comunidadeblogdopython.models import Usuario
from flask_login import login_user, logout_user, current_user, login_required
import secrets
import os
from PIL import Image

lista_usuarios = {'Ademilson', 'Elayne', 'Kerolayne'}  # lista de teste


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/contato')
def contato():
    return render_template('contato.html')


@app.route('/listagem-usuarios')
@login_required
def usuarios():
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)

@app.route('/login',methods=['GET','POST'])
def login():
    form_login = FormLogin()
    form_criarconta = FormCriarConta()
    if form_login.validate_on_submit() and 'botao_submit_login' in request.form:
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
            login_user(usuario, remember=form_login.lembrar_dados.data)
            # fez login com sucesso
            flash(f'Login feito com sucesso: {form_login.email.data}','alert-success')
            par_next = request.args.get('next')
            if par_next:
                return redirect(par_next)
            else:
                return redirect(url_for('home'))
            #return redirect(url_for('home'))

        else:
            flash('Falha no Login, E-mail ou senha incorretos', 'alert-danger')
    if form_criarconta.validate_on_submit() and 'botao_submit_criar_conta' in request.form:
        senha_cript = bcrypt.generate_password_hash(form_criarconta.senha.data)
        usuario = Usuario(username=form_criarconta.username.data, email=form_criarconta.email.data, senha=senha_cript)
        database.session.add(usuario)
        database.session.commit()
        # adicionar a sessão
        #commit da sessao

        flash(f'Conta criada com sucesso para o email: {form_criarconta.email.data}', 'alert-success')

    return render_template('login.html', form_login=form_login, form_criarconta=form_criarconta)

@app.route('/sair')
@login_required
def sair():
    logout_user()
    flash('Logout feito com sucesso', 'alert-success')
    return redirect(url_for('home'))



@app.route('/perfil')
@login_required
def perfil():
    foto_perfil = url_for('static', filename = '/fotos_perfil/{}'.format(current_user.foto_perfil))
    return render_template('perfil.html', foto_perfil=foto_perfil)



@app.route('/post/criar')
@login_required
def criar_post():
    return render_template('criarpost.html')

def salvar_imagem(imagem):
    codigo = secrets.token_hex(8) # adicionar um codigo aleatorio no nome da imagem
    nome, extensao = os.path.splitext(imagem.filename) #reduzir o tamanho da imagem
    nome_arquivo = nome + codigo + extensao # salvar imagem na pasta fotos_perfil
    caminho_completo = os.path.join(app.root_path, 'static/fotos_perfil',nome_arquivo) # mudar o campo foto_perfil no usuario para o nome da imagem nova
    tamanho = (400, 400)
    imagem_reduzida = Image.open(imagem) #reduzir imagem
    imagem_reduzida.thumbnail(tamanho) #reduzir imagem
    imagem_reduzida.save(caminho_completo) #salvar imagem


    return nome_arquivo


@app.route('/perfil/editar',methods=['GET','POST'])
@login_required
def editar_perfil():
    form = FormEditarPerfil()
    if form.validate_on_submit():
        current_user.email = form.email.data
        current_user.username = form.username.data
        #salvando imagem(usando a função salvar imagem)
        if form.foto_perfil.data:
            nome_imagem = salvar_imagem(form.foto_perfil.data)
            current_user.foto_perfil = nome_imagem

        database.session.commit()
        flash(f'Perfil atualizado com sucesso', 'alert-success')
        return redirect(url_for('perfil'))
    elif request.method == "GET":
        form.email.data = current_user.email
        form.username.data = current_user.username

    foto_perfil = url_for('static', filename='/fotos_perfil/{}'.format(current_user.foto_perfil))
    return render_template('editarperfil.html', foto_perfil=foto_perfil, form=form)



