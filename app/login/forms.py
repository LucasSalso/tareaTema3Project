from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, PasswordField
from flask_wtf.file import FileRequired, FileAllowed, FileField
from wtforms.validators import DataRequired, Length, ValidationError


class LoginForm(FlaskForm):
    username = StringField(label="Nombre de usuario", validators=[
        DataRequired(message="El nombre de usuario es obligatorio"),
        Length(max=15, message="El nombre de usuario no puede ser superior a 15 caracteres")
    ])

    password = PasswordField(label="Contraseña", validators=[
        DataRequired(message="La contraseña es obligatoria"),
        Length(min=8, message="La contraseña no puede ser inferior a 8 caracteres")
    ])


class RegisterForm(FlaskForm):

    username = StringField(label="Nombre de usuario", validators=[
        DataRequired(message="El nombre de usuario es obligatorio"),
        Length(max=15, message="El nombre de usuario no puede ser superior a 15 caracteres")
    ])

    password = PasswordField(label="Contraseña", validators=[
        DataRequired(message="La contraseña es obligatoria"),
        Length(min=8, message="La contraseña no puede ser inferior a 8 caracteres")
    ])
    passwordRepeat = PasswordField(label="Repita la contraseña", validators=[
        DataRequired(message="La repetición de la contraseña es obligatoria"),
        Length(min=8, message="La contraseña no puede ser inferior a 8 caracteres")
    ])

    nombre = StringField(label="Nombre", validators=[
        DataRequired(message="El nombre es obligatorio"),
        Length(max=20, message="El nombre no puede ser superior a 10 caracteres")
    ])

    apellidos = StringField(label="Apellidos", validators=[
        DataRequired(message="Los apellidos son obligatorio"),
        Length(max=50, message="Los apellidos no pueden superar los 50 caracteres")
    ])

    def validate_password(form,field):

        hasAnyUpperCase = False
        hasAnySpecialChar = False
        hasAnyDigit = False

        for caracter in field.data:

            # checking for uppercase character and flagging
            if caracter.isdigit():
                hasAnyDigit = True
            elif caracter.isupper():
                hasAnyUpperCase = True
            elif not caracter.isalnum():
                hasAnySpecialChar = True

        if not(hasAnyUpperCase and hasAnySpecialChar and hasAnyDigit):
            raise ValidationError("La contraseña no cumple con los patrones de seguridad")
        if field.data != form.passwordRepeat.data:
            raise ValidationError("No coinciden las contraseñas")

    def validate_passwordRepeat(form, field):
        if field.data != form.password.data:
            raise ValidationError("No coinciden las contraseñas")