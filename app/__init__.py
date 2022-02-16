from flask import Flask

app = Flask(__name__)

# Settings
app.config['SECRET_KEY'] = 'secret'

from .public import public
from .private import private

def create_app():
    app.register_blueprint(public)
    app.register_blueprint(private)
    return  app