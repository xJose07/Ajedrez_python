from ..Figura import *


class Peon_B(Figura):
    def __init__(self):
        Figura.__init__(self)
        self.simbol = "♟"
        self.nombre = "Peon Blanco"
        self.primerMovimiento = True

    def EsFiguraEnemiga(self, filaFinal, columnaFinal, jugadorNoActivo):
        figuraEsEnemiga = False
        for figura in jugadorNoActivo.diccionario.values():                  #diccionario.values() nos devuelve una lista con los valores. Debemos entrar dentro de esa lista y entonces mirar si en las listas con las figuras está la que buscamos ej: [[figura torre1, figura torre2], [figura caballo1, figura caballo 2], etc]
            if self.tab[filaFinal][columnaFinal] in figura:
                figuraEsEnemiga = True
        return figuraEsEnemiga
        
    def movimientoFiguraValido(self, filaInicial, columnaInicial, filaFinal, columnaFinal, figuraEnemiga):
        coordInicial =filaInicial,self.indexf.index(columnaInicial) #devolvemos la fila y la columna para poder trabajar con las coordenadas en el tablero
        coordFinal =filaFinal,self.indexf.index(columnaFinal) #devolvemos la fila y la columna para poder trabajar con las coordenadas en el tablero

        movimientoValido = False
        if coordFinal[1] == coordInicial[1]:
            if coordFinal[0] == coordInicial[0] -1:
                movimientoValido = True
                self.primerMovimiento = False
            if coordFinal[0] == coordInicial[0] -2 and self.primerMovimiento:
                movimientoValido = True
                self.primerMovimiento = False
        if (coordFinal[1] == coordInicial[1] +1 or coordFinal[1] == coordInicial[1] -1) and figuraEnemiga:
            if coordFinal[0] == coordInicial[0] -1:
                movimientoValido = True
                self.primerMovimiento = False
            if coordFinal[0] == coordInicial[0] -2 and self.primerMovimiento:
                movimientoValido = True
                self.primerMovimiento = False
        return movimientoValido
        
        