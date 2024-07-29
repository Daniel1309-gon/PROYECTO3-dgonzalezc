from flask import request, render_template, redirect, url_for, make_response, jsonify
from flask_login import LoginManager, login_required, login_user, current_user, logout_user
from dotenv import load_dotenv
from models.usuario import Usuario
from controllers.rutas_productos import iniciar_rutas_productos
from controllers.rutas_ingredientes import iniciar_rutas_ingredientes
from controllers.productos_controller import ProductosController

from db import db
import os
from aplicacion import app, api



load_dotenv()

secret_key = os.urandom(24)
app.config["SECRET_KEY"] = secret_key
login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = 'view'

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(user_id)
    

@app.route("/")
def main():
    return "Ingresé al sistema"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        username = request.form['username']
        password = request.form['password']
        user = Usuario.query.filter_by(username=username, password=password).first()
        if user:

            login_user(user)
            if user.is_admin:
                
                return redirect(url_for("productoscontroller"))
            else:
                return "Ingresaste con exito al sistema"
        
    return render_template("login.html")

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/not_authorized')
def not_authorized():
    return render_template("not_authorized.html"), 401
iniciar_rutas_productos(app)
iniciar_rutas_ingredientes(app)

api.add_resource(ProductosController, '/productos')

