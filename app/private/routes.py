from flask import render_template, request
from .forms import ClienteForm

from . import private

@private.route("/indexcliente/", methods=["GET","POST"])
def indexcliente():
    form = ClienteForm()
    if request.method == 'POST':
        form.validate_on_submit()
    return render_template("indexcliente.html", form=form)