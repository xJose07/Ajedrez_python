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
        movimientoValido = False
        if columnaFinal == columnaInicial:
            if filaFinal == filaInicial -1:
                movimientoValido = True
                self.primerMovimiento = False
            if filaFinal == filaInicial -2 and self.primerMovimiento:
                movimientoValido = True
                self.primerMovimiento = False
        if (columnaFinal == columnaInicial +1 or columnaFinal == columnaInicial -1) and figuraEnemiga:
            if filaFinal == filaInicial -1:
                movimientoValido = True
                self.primerMovimiento = False
            if filaFinal == filaInicial -2 and self.primerMovimiento:
                movimientoValido = True
                self.primerMovimiento = False
        return movimientoValido
        
        