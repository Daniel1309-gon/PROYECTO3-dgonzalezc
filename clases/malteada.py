from clases.iProducto import iProducto
from clases.ingrediente import Ingrediente

class Malteada(iProducto):
    def __init__(self, nombre: str, precioPublico: float, volumen: int, ingredientes: list[Ingrediente]) -> None:
        self._nombre = nombre
        self._precioPublico = precioPublico
        self._volumen = volumen
        self._ingredientes = ingredientes
        self._tipo = 'Malteada'
    
    def calcularCosto(self) -> float:
        return round(sum(ingrediente.getPrecio() for ingrediente in self._ingredientes),2) + 500
    
    def calcularCalorias(self) -> int:
        return sum(ingrediente.getCalorias() for ingrediente in self._ingredientes) + 200
    
    def calcularRentabilidad(self) -> float:
        return self._precioPublico - self.calcularCosto()
    
    def getNombre(self):
        return self._nombre
    
    def getTipo(self):
        return self._tipo
    
    def setNombre(self, nuevoNombre: str):
        self._nombre = nuevoNombre
        
    def getprecioPublico(self):
        return self._precioPublico
    
    def setprecioPublico(self, nuevoprecioPublico: float):
        self._precioPublico = nuevoprecioPublico
        
    def getVolumen(self):
        return self._volumen
    
    def setVolumen(self, nuevoVolumen: int):
        self._volumen = nuevoVolumen
        
    def getIngredientes(self) -> list[Ingrediente]:
        return self._ingredientes
    
    def setIngredientes(self, nuevosIngredientes: list[Ingrediente]):
        self._ingredientes = nuevosIngredientes
    