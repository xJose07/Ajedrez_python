from ..Figura import *
class Rey(Figura):
    def __init__(self, color):
        Figura.__init__(self)
        self.color = color
        self.simbolN = "♔"
        self.simbol = "♚"
        
    def getSimbol(self):
        if self.color == "white":
            return self.simbol
        elif self.color == "black":
            return self.simbolN   