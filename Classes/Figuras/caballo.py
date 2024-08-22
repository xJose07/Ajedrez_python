from ..Figura import *
class Caballo(Figura):
    def __init__(self,color):
        Figura.__init__(self)
        self.simbolN = "♘"        
        self.simbol = "♞"
        self.color = color
        self.nombre = "Caballo" + self.color
        
    def getSimbol(self):
        if self.color == "Blanco":
            return self.simbol
        elif self.color == "Negro":
            return self.simbolN   
        
    def movimientoFiguraValido(self, filaInicial, columnaInicial, filaFinal, columnaFinal, figuraEnemiga):
        coordInicial =filaInicial,self.indexf.index(columnaInicial) #devolvemos la fila y la columna para poder trabajar con las coordenadas en el tablero
        coordFinal =filaFinal,self.indexf.index(columnaFinal) #devolvemos la fila y la columna para poder trabajar con las coordenadas en el tablero

        movimientoValido = False
        if (coordFinal[1] == coordInicial[1] + 2) or (coordFinal[1] == coordInicial[1] - 2):  #Comprobamos que no se ha realizado un cambio de columna. En este caso, no podemos eliminar l figura enemiga que está justo delante del peón
            if (coordFinal[0] == coordInicial[0] -1) or (coordFinal[0] == coordInicial[0] +1):                           #Comprobamos que el cambio de fila es de 1 en el sentido correcto
                movimientoValido = True

        if (coordFinal[0] == coordInicial[0] + 2) or (coordFinal[0] == coordInicial[0] - 2):  #Comprobamos que no se ha realizado un cambio de columna. En este caso, no podemos eliminar l figura enemiga que está justo delante del peón
            if (coordFinal[1] == coordInicial[1] -1) or (coordFinal[1] == coordInicial[1] +1):                           #Comprobamos que el cambio de fila es de 1 en el sentido correcto
                movimientoValido = True
        return movimientoValido