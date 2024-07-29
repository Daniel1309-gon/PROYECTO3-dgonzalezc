from models.model_ingrediente import Ingrediente
from clases.iProducto import iProducto
from aplicacion import app
from db import db
from models.model_producto import Producto
from sqlalchemy.exc import SQLAlchemyError

class Heladeria:
    def __init__(self):
        self._productos = []
        self._ingredientes = []
        self._ventas_del_dia = 0
    
    def producto_mas_rentable(self):
        with app.app_context():
            try:
                productos = db.session.query(Producto).all()
                return max(productos, key=lambda producto: producto.calcularRentabilidad()).nombre
            except:
                raise SQLAlchemyError('Error en conexion')
    
    
    def vender(self, nombre_producto: str):
        with app.app_context():
            try:
                producto = db.session.query(Producto).filter_by(nombre=nombre_producto).first()
                if not producto:
                    raise ValueError('Este producto no existe')

                ingredientes = [producto.ingrediente1, producto.ingrediente2, producto.ingrediente3]
                
                for ingrediente in ingredientes:
                    if ingrediente.inventario < 1:
                        raise ValueError(f"¡Oh no! Nos hemos quedado sin {ingrediente.nombre}")

                for ingrediente in ingredientes:
                    ingrediente.inventario -= 1
                    db.session.add(ingrediente)

                db.session.commit()
                self._ventas_del_dia += 1
                return "¡Vendido!"
            
            except SQLAlchemyError as e:
                db.session.rollback()
                raise e
    
    def getProductos(self) -> list[Producto]:
        with app.app_context():
            try:
                productos = db.session.query(Producto).all()
                return productos
            except:
                raise SQLAlchemyError('Error en conexion')
    
    def setProductos(self, nuevosProductos: list[Producto]):
        self._productos = nuevosProductos
        
    
    def getIngredientes(self):
        return self._ingredientes
    
    def setIngredientes(self, nuevosIngredientes: list[Ingrediente]):
        self._ingredientes = nuevosIngredientes
    
    def getVentasDia(self):
        return self._ventas_del_dia
    
    def setVentasDia(self, nuevasVentas: int):
        self._ventas_del_dia = nuevasVentas
        
    def abastecerIngrediente(self, id: int, quantity: int):
        with app.app_context():
            try:
                ingrediente = Ingrediente.query.get(id)
                if ingrediente is None:
                    raise ValueError('Ingrediente no encontrado')
                
                ingrediente.inventario = quantity
                db.session.add(ingrediente)
                db.session.commit()
                return f'Inventario actualizado.'
            except Exception as e:
                db.session.rollback()
                return e
    
