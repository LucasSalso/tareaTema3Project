from flask import render_template, request
from .forms import ClienteForm

from . import private
from ..__init__ import engine

@private.route("/indexcliente/", methods=["GET","POST"])
def indexcliente():
    sql = f"SELECT * FROM clientes"
    with engine.connect() as conn:
        clientes = {}#conn.execute(sql)
        return render_template("indexcliente.html", clientes=clientes)

@private.route("/crearcliente/", methods=["GET","POST"])
def crearcliente():
    form = ClienteForm()
    return render_template("crearcliente.html", form=form)