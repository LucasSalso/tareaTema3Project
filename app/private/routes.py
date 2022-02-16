from flask import render_template, request
from .forms import ClienteForm

from . import private

@private.route("/indexcliente/", methods=["GET","POST"])
def indexcliente():
    sql = f"SELECT * FROM clientes"


@private.route("/crearcliente/", methods=["GET","POST"])
def crearcliente():
    form = ClienteForm()
    return render_template("crearcliente.html", form=form)