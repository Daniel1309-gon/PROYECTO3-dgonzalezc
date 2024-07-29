from abc import ABC, abstractmethod

class Ingrediente(ABC):
    
    def __init__(self, nombre: str, precio: float, calorias: int, inventario: int, esVegetariano: bool) -> None:
        self._nombre = nombre
        self._precio = precio
        self._calorias = calorias
        self._inventario = inventario
        self._esVegetariano =esVegetariano
        
    def esSano(self) -> bool:
        return self._calorias < 100 or self._esVegetariano
    
    @abstractmethod
    def abastecer(self) -> None:
        pass
    
    
    # SETTER Y GETTER
    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nuevoNombre: str):
        self._nombre = nuevoNombre
    
    def getPrecio(self):
        return self._precio
    
    def setPrecio(self, nuevoPrecio: float):
        self._precio = nuevoPrecio
    
    def getCalorias(self):
        return self._calorias
    
    def setCalorias(self, nueCalorias: int):
        self._calorias = nueCalorias
    
    def getInventario(self):
        return self._inventario
    
    def setInventario(self, nueInventario: int):
        self._inventario = nueInventario
    
    def getVegetariano(self):
        return self._esVegetariano
    
    def setVegetariano(self, nuevoVege: bool):
        self._esVegetariano = nuevoVege
        
    def actInventario(self):
        self._inventario -= 1