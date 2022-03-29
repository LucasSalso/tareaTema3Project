from flask import Flask
from flask_recaptcha import ReCaptcha
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .log.logs import configureLogging

app = Flask(__name__)

logger = configureLogging(__name__)

# Settings
app.secret_key = "secret"
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost:5432/tareaTema3Project'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['RECAPTCHA_SITE_KEY'] = 'SITE_KEY'
app.config['RECAPTCHA_SECRET_KEY'] = 'SECRET_KEY'

recaptcha = ReCaptcha(app)

db = SQLAlchemy(app)
login_manager = LoginManager(app)

login_manager.login_view = "login.loginUsuario"

@app.errorhandler(413)
def too_large(e):
    return "La imagen tiene un tamaño mayor al permitido", 413

from .public import public
from .private import private
from .login import login
from .admin import admin

def create_app():
    app.register_blueprint(public)
    app.register_blueprint(private)
    app.register_blueprint(login)
    app.register_blueprint(admin)
    return  app