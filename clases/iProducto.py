from abc import ABC, abstractmethod

class iProducto(ABC):
    @abstractmethod
    def calcularCosto():
        pass
    
    @abstractmethod
    def calcularRentabilidad():
        pass
    
    @abstractmethod
    def calcularCalorias():
        pass
    