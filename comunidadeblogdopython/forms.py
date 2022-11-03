from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, length, Email, EqualTo

class FormCriarConta(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), length(6, 20)])
    confirmacao_senha = PasswordField('Confirmar Senha', validators=[DataRequired(), EqualTo('senha')])
    botao_submit_criar_conta = SubmitField('Criar Conta')


class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), length(6, 20)])
    lembrar_dados = BooleanField('Lembrar Dados de Acesso')
    botao_submit_login = SubmitField('Fazer Login')

