from flask import jsonify, request, render_template, make_response
from db import db
from models.model_producto import Producto
from models.model_ingrediente import Ingrediente
from sqlalchemy.exc import SQLAlchemyError
from controllers.decoradores import *
from flask_login import login_required

def iniciar_rutas_ingredientes(app):
      
    @app.route('/ingredientes', methods=['GET'])
    #@empleado_required
    def getIngredients():
        ingredientes = db.session.query(Ingrediente).all()
        return make_response(render_template('ingredientes.html', ingredientes=ingredientes))
    
    @app.route('/ingredientes/id/<int:id>', methods=['GET'])
    #@empleado_required
    def getIngredientByID(id: int):
        ingrediente = db.session.query(Ingrediente).filter_by(id=id).first()
        if ingrediente:
            return jsonify({
                "id": ingrediente.id,
                "nombre": ingrediente.nombre,
                "precio": ingrediente.precio,
                "calorias": ingrediente.calorias,
                "inventario": ingrediente.inventario,
                "esVegano": ingrediente.esVegano
            })
        else:
            return jsonify({"error": "Ingrediente no encontrado"}), 404
        
    @app.route('/ingredientes/nombre/<nombre>', methods=['GET'])
    #@empleado_required
    def getIngredientByName(nombre: str):
        ingrediente = db.session.query(Ingrediente).filter_by(nombre=nombre).first()
        if ingrediente:
            return jsonify({
                "id": ingrediente.id,
                "nombre": ingrediente.nombre,
                "precio": ingrediente.precio,
                "calorias": ingrediente.calorias,
                "inventario": ingrediente.inventario,
                "esVegano": ingrediente.esVegano
            })
        else:
            return jsonify({"error": "Ingrediente no encontrado"}), 404
        
    @app.route('/ingredientes/essano/<int:id>', methods=['GET'])
    #@empleado_required
    def getEsSano(id: int):
        ingrediente = db.session.query(Ingrediente).filter_by(id=id).first()
        if ingrediente:
            return jsonify({
                "id": ingrediente.id,
                "nombre": ingrediente.nombre,
                "EsSano": ingrediente.esSano()
            })
        else:
            return jsonify({"error": "Ingrediente no encontrado"}), 404
        
    @app.route('/ingredientes/abastecer/<int:id>', methods=['GET', 'POST'])
    #@empleado_required
    def abastecer(id: int):
        ingrediente = db.session.query(Ingrediente).filter_by(id=id).first()
        if ingrediente:
            ingrediente.inventario += 5
            db.session.add(ingrediente)
            db.session.commit()
            
            return jsonify({"message": f"El ingrediente {ingrediente.nombre} ha sido reabastecido"}), 200
        else:
            return jsonify({"error": "Producto no encontrado"}), 404
        
    @app.route('/ingredientes/renovar-inventario/<int:id>', methods=['GET', 'POST'])
    #@empleado_required
    def renovarInventario(id: int):
        ingrediente = db.session.query(Ingrediente).filter_by(id=id).first()
        if ingrediente:
            ingrediente.inventario = 0
            db.session.add(ingrediente)
            db.session.commit()
            
            return jsonify({"message": f"Se ha renovado el inventario satisfactoriamente"}), 200
        else:
            return jsonify({"error": "Producto no encontrado"}), 404
    