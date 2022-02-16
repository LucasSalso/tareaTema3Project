from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import create_engine

app = Flask(__name__)

# Settings
app.config['SECRET_KEY'] = 'secret'

#Establecer la cadena de conexión
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost:5432/tareaTema3Project'
#Desactivamos la gestión de notificaciones de SQLAlchemy
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#Instanciamos un objeto de la clase SQLAlchemy
db = SQLAlchemy(app)
#Instanciar un objeto de la clase Migrate
migrate = Migrate(app,db)

engine = create_engine("postgresql://postgres:123456@localhost:5432/tareaTema3Project")

#Importamos el modelo
from app.private import models

from .public import public
from .private import private

def create_app():
    app.register_blueprint(public)
    app.register_blueprint(private)
    return  app