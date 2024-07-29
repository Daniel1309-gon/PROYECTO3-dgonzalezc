from clases.ingrediente import Ingrediente

class Complemento(Ingrediente):
    def __init__(self, nombre: str, precio: float, calorias: int, inventario: int, esVegetariano: bool) -> None:
        super().__init__(nombre, precio, calorias, inventario, esVegetariano)
        
    def abastecer(self) -> None:
        self._inventario += 10
        
    def renovarInventario(self):
        self._inventario = 0