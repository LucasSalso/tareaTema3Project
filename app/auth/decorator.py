from functools import wraps

from flask_login import current_user
from werkzeug.exceptions import abort

import app


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kws):
        is_admin = getattr(current_user, 'isAdmin', False)
        if not is_admin:
            app.logger.warning(getattr(current_user, 'username') + " esta queriendo acceder a un recurso que es de admin.")
            abort(401)
        return f(*args, **kws)
    return decorated_function