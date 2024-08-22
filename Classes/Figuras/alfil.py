from ..Figura import *
class Alfil(Figura):
    def __init__(self, color):
        Figura.__init__(self)
        self.simbolN = "♗"        
        self.simbol = "♝"
        self.color = color
        
    def getSimbol(self):
        if self.color == "Blanco":
            return self.simbol
        elif self.color == "Negro":
            return self.simbolN   

        

    