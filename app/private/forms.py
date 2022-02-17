from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired
from wtforms import StringField, FileField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

class ClienteForm(FlaskForm):
    dni = StringField('D.N.I', validators=[DataRequired('El D.N.I es obligatorio'), Length(max=10)])
    nombre = StringField('Nombre', validators=[DataRequired('El Nombre es obligatorio'), Length(max=20)])
    apellidos = StringField('Apellidos', validators=[DataRequired('Los Apellidos son obligatorios'), Length(max=50)])
    imagen = FileField('Imagen', validators=[FileRequired(message='El archivo no es valido'),
                                             FileAllowed(['jpg', 'png'], message='Solo jpg y png')])

    submit = SubmitField(label="Enviar")

    def validate_imagen(form, field):
        max_length = 1024 * 1024
        if len(field.data.read()) > max_length:
            raise ValidationError(f"El fichero no puede ser superior a {max_length}")