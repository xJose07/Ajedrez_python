from ..Figura import *


class Peon_B(Figura):
    def __init__(self):
        Figura.__init__(self)
        self.simbol = "♟"
        self.nombre = "Peon Blanco"
        self.primerMovimiento = True
    
        
    def movimientoFiguraValido(self, filaInicial, columnaInicial, filaFinal, columnaFinal, figuraEnemiga):
        coordInicial =filaInicial,self.indexf.index(columnaInicial) #devolvemos la fila y la columna para poder trabajar con las coordenadas en el tablero
        coordFinal =filaFinal,self.indexf.index(columnaFinal) #devolvemos la fila y la columna para poder trabajar con las coordenadas en el tablero

        movimientoValido = False
        if coordFinal[1] == coordInicial[1] and not figuraEnemiga:            #Comprobamos que no se ha realizado un cambio de columna. En este caso, no podemos eliminar l figura enemiga que está justo delante del peón
            if coordFinal[0] == coordInicial[0] -1:                           #Comprobamos que el cambio de fila es de 1 en el sentido correcto
                movimientoValido = True
                self.primerMovimiento = False
            if coordFinal[0] == coordInicial[0] -2 and self.primerMovimiento:
                movimientoValido = True
                self.primerMovimiento = False
        if (coordFinal[1] == coordInicial[1] +1 or coordFinal[1] == coordInicial[1] -1) and figuraEnemiga:      #Comprobamos que solo se realiza un cambio de columna para eliminar una figura enemiga
            if coordFinal[0] == coordInicial[0] -1:
                movimientoValido = True
                self.primerMovimiento = False
        return movimientoValido
        
        