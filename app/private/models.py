from ..__init__ import db

class Cliente(db.Model):
    dni = db.Column(db.String(10), unique=True, primary_key=True, nullable=False)
    nombre = db.Column(db.String(20), nullable=False)
    apellidos = db.Column(db.String(50), nullable=False)
    imagen = db.Column(db.String(50), nullable=False)

    def recuperarClientes(self, dni=None):
        if dni == None:
            return Cliente.query.all()
        else:
            return Cliente.query.filter_by(dni=dni)

    def guardarCliente(self):
        db.session.add(self)
        db.session.commit()

db.create_all()
