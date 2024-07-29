from clases.iProducto import iProducto
from clases.ingrediente import Ingrediente


class Copa(iProducto):
    def __init__(self, nombre: str, precioPublico: float, tipoVaso: str, ingredientes: list[Ingrediente]) -> None:
        self._nombre = nombre
        self._precioPublico = precioPublico
        self._tipoVaso = tipoVaso
        self._ingredientes = ingredientes
        self._tipo = 'Copa'
    
    def calcularCosto(self) -> float:
        return round(sum(ingrediente.getPrecio() for ingrediente in self._ingredientes),2)
    
    def calcularCalorias(self) -> int:
        return sum(ingrediente.getCalorias() for ingrediente in self._ingredientes)
    
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
    
    def setPrecioPublico(self, nuevoprecioPublico: float):
        self._precioPublico = nuevoprecioPublico
        
    def getTipoVaso(self):
        return self._tipoVaso
    
    def setTipoVaso(self, nuevoVaso: str):
        self._tipoVaso = nuevoVaso
        
    def getIngredientes(self) -> list[Ingrediente]:
        return self._ingredientes
    
    def setIngredientes(self, nuevosIngredientes: list[Ingrediente]):
        self._ingredientes = nuevosIngredientes
    