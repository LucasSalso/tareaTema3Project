from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost:5432/tareaTema3Project'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Cliente(db.Model):
    dni = db.Column(db.String(10), unique=True, primary_key=True, nullable=False)
    nombre = db.Column(db.String(20), nullable=False)
    apellidos = db.Column(db.String(50), nullable=False)
    imagen = db.Column(db.String(50), nullable=False)

    def __init__(self, dni, nombre, apellidos, imagen):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos
        self.imagen = imagen

db.create_all()
