from flask import render_template, abort
from flask_login import login_required, current_user

from . import admin
from ..auth.decorator import admin_required
from ..login.models import Usuario


@admin.route('/listadoUsuarios/')
@login_required
@admin_required
def listadoUsuarios():  # put application's code here
    # if not current_user.is_admin:
    #     abort(401)
    usuario = Usuario()
    usuarios = usuario.recuperarUsuarios()
    return render_template('listadoUsuarios.html', usuarios=usuarios)

