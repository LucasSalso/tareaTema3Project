from flask_wtf import FlaskForm
from wtforms import StringField, FileField
from wtforms.validators import DataRequired

class ClienteForm(FlaskForm):
    dni = StringField('D.N.I', validators=[DataRequired('El D.N.I es obligatorio')])
    nombre = StringField('Nombre', validators=[DataRequired('El Nombre es obligatorio')])
    apellidos = StringField('Apellidos', validators=[DataRequired('Los Apeliidos son obligatorios')])
    imagen = FileField('Imagen', validators=[DataRequired('La Imagen es obligatoria')])