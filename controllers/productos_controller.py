from flask import render_template, make_response
from flask_restful import Resource

from db import db

class ProductosController(Resource):
    def get(self):
        
        return make_response(render_template("productos.html"))