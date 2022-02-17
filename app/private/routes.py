from os.path import dirname, abspath, join

from flask import render_template, request
from werkzeug.utils import secure_filename

from .forms import ClienteForm
from werkzeug.datastructures import CombinedMultiDict
import os

from . import private
from .models import Cliente

@private.route("/indexcliente/", methods=["GET","POST"])
def indexcliente():
    clientes = Cliente().recuperarClientes()
    return render_template("indexcliente.html", clientes=clientes)

@private.route("/crearcliente/", methods=["GET","POST"])
def crearcliente():
    form = ClienteForm(CombinedMultiDict((request.files, request.form)))
    if form.validate_on_submit():
        dni = request.form.get("dni")
        nombre = request.form.get("nombre")
        apellidos = request.form.get("apellidos")

        BASE_DIR = dirname(dirname(abspath(__file__)))
        UPLOAD_DIR = join(BASE_DIR, 'upload')
        filename = secure_filename(form.imagen.data.filename)
        form.imagen.data.save(UPLOAD_DIR + "/" + filename)

        cliente = Cliente()
        cliente.dni = dni
        cliente.nombre = nombre
        cliente.apellidos = apellidos
        cliente.imagen = dni + "." + filename.split(".")[1]
        cliente.guardarCliente()

        return form.nombre.data
    return render_template("crearcliente.html", form=form)
