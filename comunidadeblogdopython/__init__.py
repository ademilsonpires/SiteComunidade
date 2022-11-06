from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config['SECRET_KEY'] = '9e57ca58a84f6cd3b02b2114fd90ef7c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'
database = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from comunidadeblogdopython import routes