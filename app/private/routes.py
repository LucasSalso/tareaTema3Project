import base64
from os.path import dirname, abspath, join

from flask import render_template, request, url_for
from flask_login import current_user
from werkzeug.utils import secure_filename, redirect
from wtforms import ValidationError

from .forms import ClienteForm
from werkzeug.datastructures import CombinedMultiDict
import os

from . import private
from .models import Cliente

@private.route("/indexcliente/", methods=["GET","POST"])
def indexcliente():

    if not current_user.is_authenticated:
        return redirect(url_for("public.index"))

    cliente = Cliente()

    if request.method == "POST":
        dni = request.form.get("buscador_dni")
        clientes = cliente.recuperarClientes(dni)
        habilitarmostrartodosclientes = True
    else :
        clientes = cliente.recuperarClientes()
        habilitarmostrartodosclientes = False
    return render_template("indexcliente.html", clientes=clientes, habilitarmostrartodosclientes=habilitarmostrartodosclientes)

@private.route("/crearcliente/", methods=["GET","POST"])
def crearcliente():

    if not current_user.is_authenticated:
        return redirect(url_for("public.index"))

    form = ClienteForm(CombinedMultiDict((request.files, request.form)))
    if form.validate_on_submit():
        dni = request.form.get("dni")
        nombre = request.form.get("nombre")
        apellidos = request.form.get("apellidos")

        #BASE_DIR = dirname(dirname(abspath(__file__)))
        #UPLOAD_DIR = join(BASE_DIR, 'upload')
        #filename = secure_filename(form.imagen.data.filename)
        #filename = dni + "." + filename.split(".")[1]
        #form.imagen.data.save(UPLOAD_DIR + "/" + filename)

        cliente = Cliente()
        cliente.dni = dni
        cliente.nombre = nombre
        cliente.apellidos = apellidos

        encoded_bytes = base64.b64encode(form.imagen.data.read())
        encoded_string = str(encoded_bytes).replace("b'", "").replace("'", "")
        cliente.imagen = encoded_string

        cliente.guardarCliente()

        clientes = Cliente().recuperarClientes()
        return render_template("indexcliente.html", clientes=clientes, habilitarmostrartodosclientes=False)
    return render_template("crearcliente.html", form=form)
