from flask import render_template, request, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required

import app

from .models import Usuario
from .forms import RegisterForm, LoginForm
from . import login
from .. import db

@login.route("/registrarUsuario/", methods=["GET","POST"])
def registrarUsuario():

    if current_user.is_authenticated:
        return redirect(url_for('private.indexcliente'));

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
            app.logger.error("No se ha podido dar de alta " + e.__str__())
            error = "No se ha podido dar de alta " + e.__str__()
    return render_template("registrarUsuario.html", form=form, error=error)

@app.login_manager.user_loader
def loadUser(userId):
    return Usuario.get_by_id(userId)

@login.route("/loginUsuario/", methods=["GET","POST"])
def loginUsuario():
    error = ""

    if current_user.is_authenticated:
        return redirect(url_for('private.indexcliente'));

    form = LoginForm(request.form)
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = Usuario.get_by_username(username)
        if user and user.check_password(password):
            login_user(user, remember=form.recuerdame.data)
            app.logger.info("Login correcto : " + username)
            return redirect(url_for("private.indexcliente"))
        else:
            error = "Usuario y/o contraseña incorrecta"
            app.logger.warning("Login erroneo : " + username)
    return render_template("loginUsuario.html", form=form, error=error)

@login.route("/logout/")
@login_required
def logout():
    logout_user()
    app.logger.info("Logout correcto")
    return redirect(url_for("public.index"))
