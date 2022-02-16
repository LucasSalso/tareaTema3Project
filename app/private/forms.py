from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired
from wtforms import StringField, FileField
from wtforms.validators import DataRequired, Length

class ClienteForm(FlaskForm):
    dni = StringField('D.N.I', validators=[DataRequired('El D.N.I es obligatorio'), Length(max=10)])
    nombre = StringField('Nombre', validators=[DataRequired('El Nombre es obligatorio'), Length(max=20)])
    apellidos = StringField('Apellidos', validators=[DataRequired('Los Apeliidos son obligatorios'), Length(max=50)])
    imagen = FileField('Imagen', validators=[FileRequired(message='El archivo debe estar cargado'),FileAllowed(['jpg', 'png'], message='El formato del archivo de carga es incorrecto')])