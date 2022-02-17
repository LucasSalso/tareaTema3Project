from ..__init__ import db

class Cliente(db.Model):
    dni = db.Column(db.String(10), unique=True, primary_key=True, nullable=False)
    nombre = db.Column(db.String(20), nullable=False)
    apellidos = db.Column(db.String(50), nullable=False)
    imagen = db.Column(db.String(50), nullable=False)

    def recuperarClientes(self):
        return db.session.query(Cliente).all

db.create_all()
