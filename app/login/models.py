from flask_login import UserMixin

import app
from ..__init__ import db
from cryptography.fernet import Fernet
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    nombre = db.Column(db.String(20), nullable=False)
    apellidos = db.Column(db.String(50), nullable=False)
    isAdmin = db.Column(db.Boolean, default=False)

    def __str__(self):
        return f"{self.apellidos},{self.nombre}"

    def create(self):
        try:
            db.session.add(self)
            db.session.commit()
            app.logger.info("Se ha creado correctamente el usuario")
        except:
            app.logger.error("No se ha creado correctamente el usuario")
            raise

    @staticmethod
    def get_by_id(id):
        return Usuario.query.get(id)

    @staticmethod
    def get_by_username(username):
        return Usuario.query.filter_by(username=username).first()

    def set_password(self, password):
        method = "pbkdf2:sha256:260000"
        self.password = generate_password_hash(password, method=method)  # Por defecto sha256

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def recuperarUsuarios(self):
        app.logger.info("Se recupera la lista de usuarios")
        return Usuario.query.all()

db.create_all()
