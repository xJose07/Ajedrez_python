from ..Figura import *
class Peon_N(Figura):
    def __init__(self):
        Figura.__init__(self)
        self.simbol = "♙"
        self.nombre = "Peon Negro"
        self.primerMovimiento = True
        
    def movimiento(self):
        if self.primerMovimiento:
            self.primerMovimiento = False
            return [2, 0]
            
        else:
            return [1, 0]