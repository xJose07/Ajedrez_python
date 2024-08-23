from ..Figura import *
class Rey(Figura):
    def __init__(self, color):
        Figura.__init__(self)
        self.color = color
        self.simbolN = "♔"
        self.simbol = "♚"
        self.nombre = "Rey" + self.color
        
    def getSimbol(self):
        if self.color == "Blanco":
            return self.simbol
        elif self.color == "Negro":
            return self.simbolN   
    
    def movimientoFiguraValido(self, filaInicial, columnaInicial, filaFinal, columnaFinal, figuraEnemiga, figuraAmiga):
        coordInicial =filaInicial,self.indexf.index(columnaInicial) #devolvemos la fila y la columna para poder trabajar con las coordenadas en el tablero
        coordFinal =filaFinal,self.indexf.index(columnaFinal) #devolvemos la fila y la columna para poder trabajar con las coordenadas en el tablero

        movimientoValido = False
        if ((coordFinal[0] == coordInicial[0] + 1) or (coordFinal[0] == coordInicial[0] - 1)) and not figuraAmiga:    #Si se mueve la fila en 1 o -1
            if (coordFinal[1] == coordInicial[1] -1) or ((coordFinal[1] == coordInicial[1])) or (coordFinal[1] == coordInicial[1] +1):  #La columna puede moverse en -1, 0 o 1
                movimientoValido = True
    
        if ((coordFinal[1] == coordInicial[1] + 1) or (coordFinal[1] == coordInicial[0] - 1)) and not figuraAmiga:    #Si se mueve la columna en 1 o -1
            if (coordFinal[0] == coordInicial[0]):
                movimientoValido = True
        return movimientoValido