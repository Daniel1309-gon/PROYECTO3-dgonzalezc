from flask import jsonify, request, render_template, make_response
from db import db
from models.model_producto import Producto
from models.model_ingrediente import Ingrediente
from sqlalchemy.exc import SQLAlchemyError
from controllers.decoradores import *
from flask_login import login_required

def iniciar_rutas_productos(app):
    @app.route('/productos', methods=['GET'])
    def getProductos():
        productos = db.session.query(Producto).all()
        return make_response(render_template('productos.html', productos=productos))
    
    @app.route('/productos/id/<id>', methods=['GET'])
    @login_required
    def getProductbyID(id: int):
        producto = db.session.query(Producto).filter_by(id=id).first()
        if producto:
            return jsonify({
                "id": producto.id,
                "tipo": producto.tipo,
                "nombre": producto.nombre,
                "precio": producto.precio
            })
        else:
            return jsonify({"error": "Producto no encontrado"}), 404
    
    @app.route('/productos/nombre/<nombre>', methods=['GET'])
    @login_required
    def getProductbyName(nombre: str):
        producto = db.session.query(Producto).filter_by(nombre=nombre).first()
        if producto:
            return jsonify({
                "id": producto.id,
                "tipo": producto.tipo,
                "nombre": producto.nombre,
                "precio": producto.precio
            })
        else:
            return jsonify({"error": "Producto no encontrado"}), 404
        
    @app.route('/productos/calorias/<id>', methods=['GET'])
    @login_required
    def getCalbyID(id: int):
        producto = db.session.query(Producto).filter_by(id=id).first()
        
        if producto:
            return jsonify({
                "id": producto.id,
                "Calorias": sum(ingrediente.calorias for ingrediente in producto.getIngredientes())
            })
        else:
            return jsonify({"error": "Producto no encontrado"}), 404
        
    @app.route('/productos/rentabilidad/<id>', methods=['GET'])
    @admin_required
    def getRentabilidadbyID(id: int):
        producto = db.session.query(Producto).filter_by(id=id).first()
        
        if producto:
            return jsonify({
                "id": producto.id,
                "Rentabilidad": producto.calcularRentabilidad()
            })
        else:
            return jsonify({"error": "Producto no encontrado"}), 404
        
    @app.route('/productos/costo/<int:id>', methods=['GET'])
    @empleado_required
    def getCostbyID(id: int):
        producto = db.session.query(Producto).filter_by(id=id).first()
        
        if producto:
            return jsonify({
                "id": producto.id,
                "Costo": producto.calcularCosto()
            })
        else:
            return jsonify({"error": "Producto no encontrado"}), 404
    
    @app.route('/ventas/id/<int:id>', methods=['GET', 'POST'])
    @login_required
    def venderByID(id: int):
        producto = db.session.query(Producto).filter_by(id=id).first()
        if producto:
                    # Verificar el inventario de todos los ingredientes antes de descontar
            for ingrediente in producto.getIngredientes():
                if ingrediente.inventario < 1:
                    return jsonify({"error": f"¡Oh no! Nos hemos quedado sin {ingrediente.nombre}"}), 400

                    # Descontar del inventario si todos los ingredientes tienen suficiente
            for ingrediente in producto.getIngredientes():
                ingrediente.inventario -= 1
                db.session.add(ingrediente)

            db.session.commit()
            return jsonify({"message": "¡Vendido!"}), 200
        else:
            return jsonify({"error": "Producto no encontrado"}), 404