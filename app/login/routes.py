from flask import render_template, request, redirect, url_for

import app

from .models import Usuario
from .forms import RegisterForm, LoginForm
from . import login
from .. import db

@login.route("/registrarUsuario/", methods=["GET","POST"])
def registrarUsuario():
    error = ""
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        try:
            usuario = Usuario()
            usuario.username = form.username.data
            usuario.set_password(form.password.data)
            usuario.nombre = form.nombre.data
            usuario.apellidos = form.apellidos.data
            usuario.create()
            return redirect(url_for('login.loginUsuario'))
        except Exception as e:
            error = "No se ha podido dar de alta " + e.__str__()
    return render_template("registrarUsuario.html", form=form, error=error)

@login.route("/loginUsuario/", methods=["GET","POST"])
def loginUsuario():
    error = ""
    form = LoginForm(request.form)
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        usuario = Usuario.get_by_username(username)
        if usuario and usuario.check_password(password):
            return redirect(url_for("private.indexcliente"))
        else:
            error = "Usuario y/o contraseña incorrecta"
    return render_template("loginUsuario.html", form=form, error=error)

