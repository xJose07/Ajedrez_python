from ..Figura import *
class Torre(Figura):
    def __init__(self,color):
        Figura.__init__(self)
        self.simbolN = "♖"        
        self.simbol = "♜"
        self.color = color
        
    def getSimbol(self):
        if self.color == "white":
            return self.simbol
        elif self.color == "black":
            return self.simbolN   

        

    
    