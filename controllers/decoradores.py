from functools import wraps
from flask import request, jsonify, redirect, url_for, session
from flask_login import current_user

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            return jsonify({"error": "No autorizado"}), 401
        return f(*args, **kwargs)
    return decorated_function

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            return redirect(url_for('not_authorized'))
        return f(*args, **kwargs)
    return decorated_function

def empleado_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not (current_user.is_admin or current_user.is_empleado):
            return redirect(url_for('not_authorized'))
        return f(*args, **kwargs)
    return decorated_function

