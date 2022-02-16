from ..__init__ import db

class Cliente(db.Model):
    dni = db.Column(db.String(10), primary_key=True)
    nombre = db.Column(db.String(20), nullable=False)
    apellidos = db.Column(db.String(50), nullable=False)
    imagen = db.Column(db.String(50), nullable=False)

    def __init__(self, dni, nombre, apellidos, imagen):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos
        self.imagen = imagen

