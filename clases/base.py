from clases.ingrediente import Ingrediente

class Base(Ingrediente):
    def __init__(self, nombre: str, precio: float, calorias: int, inventario: int, esVegetariano: bool, sabor: str) -> None:
        super().__init__(nombre, precio, calorias, inventario, esVegetariano)
        self._sabor = sabor
        
    def abastecer(self) -> None:
        self._inventario += 5
        
    def getSabor(self):
        return self._sabor
    
    def setSabor(self, nuevoSabor: str):
        self._sabor = nuevoSabor