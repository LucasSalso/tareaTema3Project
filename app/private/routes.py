from flask import render_template, request
from .forms import ClienteForm

from . import private
from .models import Cliente

@private.route("/indexcliente/", methods=["GET","POST"])
def indexcliente():
    clientes = Cliente().recuperarClientes()
    return render_template("indexcliente.html", clientes=clientes)

@private.route("/crearcliente/", methods=["GET","POST"])
def crearcliente():
    form = ClienteForm()
    return render_template("crearcliente.html", form=form)