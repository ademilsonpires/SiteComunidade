from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY'] = '9e57ca58a84f6cd3b02b2114fd90ef7c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'
database = SQLAlchemy(app)

from comunidadeblogdopython import routes