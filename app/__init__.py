from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Settings
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost:5432/tareaTema3Project'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024

db = SQLAlchemy(app)

@app.errorhandler(413)
def too_large(e):
    return "La imagen tiene un tamaño mayor al permitido", 413

from .public import public
from .private import private

def create_app():
    app.register_blueprint(public)
    app.register_blueprint(private)
    return  app