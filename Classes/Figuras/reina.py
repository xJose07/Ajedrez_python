from ..Figura import *
class Reina(Figura):
    def __init__(self, color):
        Figura.__init__(self)
        self.simbolN = "♕"        
        self.simbol = "♛"
        self.color = color
        self.nombre = "Reina" + self.color
        
    def getSimbol(self):
        if self.color == "Blanco":
            return self.simbol
        elif self.color == "Negro":
            return self.simbolN   

    def movimientoFiguraValido(self, filaInicial, columnaInicial, filaFinal, columnaFinal, figuraEnemiga, figuraAmiga):
        coordInicial =filaInicial,self.indexf.index(columnaInicial) #devolvemos la fila y la columna para poder trabajar con las coordenadas en el tablero
        coordFinal =filaFinal,self.indexf.index(columnaFinal) #devolvemos la fila y la columna para poder trabajar con las coordenadas en el tablero

        movimientoValido = False
        if (coordFinal[0] == coordInicial[0]) and (coordFinal[1] != coordInicial[1]) and not figuraAmiga:
            movimientoValido = True
    
        if (coordFinal[1] == coordInicial[1]) and (coordFinal[0] != coordInicial[0]) and not figuraAmiga:
            movimientoValido = True

        if (coordFinal[0] != coordInicial[0]) and (coordFinal[1] != coordInicial[1]) and (abs(coordFinal[0] - coordInicial[0]) == abs(coordFinal[1] - coordInicial[1])) and not figuraAmiga:
            movimientoValido = True
            
        return movimientoValido    