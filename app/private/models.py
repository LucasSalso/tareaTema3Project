from sqlalchemy.exc import IntegrityError

from ..__init__ import db

class Cliente(db.Model):
    dni = db.Column(db.String(10),primary_key=True)
    nombre = db.Column(db.String(20),nullable=False)
    apellidos = db.Column(db.String(50),nullable=False)
    imagen = db.Column(db.String,nullable=False)
    def save(self):
        try:
            if not self.id:
                db.session.add(self)
                db.session.commit()
        except IntegrityError:
            raise Exception("Error: ya existe un cliente con el mismo DNI")
