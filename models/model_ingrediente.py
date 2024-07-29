from db import db
from aplicacion import app

class Ingrediente(db.Model):
    __tablename__ = 'ingredientes'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(45), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    calorias = db.Column(db.Integer, nullable=False)
    inventario = db.Column(db.Integer, nullable=False)
    esVegano = db.Column(db.Boolean, nullable=False)
    
    def getPrecio(self):
        return self.precio
    
    def esSano(self):
        return self.esVegano or self.calorias < 100
    
    def getCalorias(self):
        return self.calorias
    
    def abastecer(self) -> None:
        self.inventario += 5
    
    def renovarInventario(self):
        self.inventario = 0
    
    
    
def insertar_ingrediente(nombre: str, precio: float, calorias: int, inventario: int, esVegano: bool):
    with app.app_context():
        ingrediente = Ingrediente(
            nombre=nombre, precio=precio, calorias=calorias, inventario=inventario, esVegano=esVegano)
        db.session.add(ingrediente)
        db.session.commit()
        return 'Ingrediente agregado correctamente'
    