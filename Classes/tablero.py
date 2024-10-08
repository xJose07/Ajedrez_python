from Classes.Figuras.Torre import Torre
from Classes.Figuras.Caballo import Caballo
from Classes.Figuras.Alfil import Alfil
from Classes.Figuras.Peon_B import Peon_B
from Classes.Figuras.Peon_N import Peon_N
from Classes.Figuras.Rey import Rey
from Classes.Figuras.Reina import Reina
from Classes.Figura import Figura

class Tablero():
    def __init__(self, jugador1, jugador2):
        self.tab=self.crearTablero()
        self.indexf=list('ABCDEFGH')
        self.jugador1 = jugador1
        self.jugador2 = jugador2

    def crearTablero(self):
        tab=[]
        for i in range(8):
            fila=[]
            for j in range(8):
                fila.append('-')
            tab.append(fila)  
        return tab

    def imprimirTablero(self):
        s =" "
        print(s,*self.indexf,end=s)
        print()
        
        for i in range(len(self.tab)):
            print(i,end=s)
            for j in range(len(self.tab[0])):
                if isinstance(self.tab[i][j], Figura):
                    print(self.tab[i][j].getSimbol(),end=s)
                else:
                    print(self.tab[i][j][0],end=s)
            print()
            
    def traducirIndice(self,fila,col):
        return fila,self.indexf.index(col) #devolvemos la fila y la columna para poder trabajar con las coordenadas en el tablero
    
    def filaOK(self, f):
        return f in range(8)

    def colOK(self, col):
        if len(col) == 1:
            return col in self.indexf
        else:
            return False
       
    #Comprobar si la casilla está vacia (al colocar las figuras despues del input del usuario)

    def areaVacia(self,x,y):
        coord = self.traducirIndice(x,y)

        buida = False
        if self.tab[coord[0]][coord[1]] == '-':
            buida = True
        return buida
    
    def colocarFichasInicializacion(self, color1, color2, jugador1, jugador2):
        for i in range(2):
            if i == 0:
                for j in range(8):
                    if j == 0:
                        self.tab[i][j] = jugador2.diccionario['torre'][0]#poner aqui los 'objetos/fichas' de una de las torres
                    if j==7:
                        self.tab[i][j] = jugador2.diccionario['torre'][1]#poner aqui los 'objetos/fichas' de una de las torres
                    if j == 1:
                        self.tab[i][j] = jugador2.diccionario['caballo'][0]#poner aqui los 'objetos/fichas' de uno de los caballos
                    if j == 6:
                        self.tab[i][j] = jugador2.diccionario['caballo'][1]#poner aqui los 'objetos/fichas' de uno de los caballos
                    if j == 2:
                        self.tab[i][j] = jugador2.diccionario['alfil'][0]#poner aqui los 'objetos/fichas' de uno de los alfiles
                    if j == 5:
                        self.tab[i][j] = jugador2.diccionario['alfil'][1]#poner aqui los 'objetos/fichas' de uno de los alfiles
                    if j == 3:
                        self.tab[i][j] = jugador2.diccionario['rey'][0]#poner aqui los 'objetos/fichas' del rey
                    if j == 4:
                        self.tab[i][j] = jugador2.diccionario['reina'][0]#poner aqui los 'objetos/fichas' de la reina
            if i == 1:
                for j in range(8):
                    self.tab[i][j] = jugador2.diccionario['peon_N'][j]#poner aqui los 'objetos/fichas' de los peones negros
        for i in range(6, 8):
            if i == 6:
                for j in range(8):
                    self.tab[i][j] = jugador1.diccionario['peon_B'][j]#poner aqui los 'objetos/fichas' de los peones blancos
            if i == 7:
                for j in range(8):
                    if j == 0:
                        self.tab[i][j] = jugador1.diccionario['torre'][0]#poner aqui los 'objetos/fichas' de una de las torres
                    if j == 7:
                        self.tab[i][j] = jugador1.diccionario['torre'][1]#poner aqui los 'objetos/fichas' de una de las torres
                    if j == 1:
                        self.tab[i][j] = jugador1.diccionario['caballo'][0]#poner aqui los 'objetos/fichas' de uno de los caballos
                    if j == 6:
                        self.tab[i][j] = jugador1.diccionario['caballo'][1]#poner aqui los 'objetos/fichas' de uno de los caballos
                    if j == 2:
                        self.tab[i][j] = jugador1.diccionario['alfil'][0]#poner aqui los 'objetos/fichas' de uno de los alfiles
                    if j == 5:
                        self.tab[i][j] = jugador1.diccionario['alfil'][1]#poner aqui los 'objetos/fichas' de uno de los alfiles
                    if j == 3:
                        self.tab[i][j] = jugador1.diccionario['reina'][0]#poner aqui los 'objetos/fichas' de la reina
                    if j == 4:
                        self.tab[i][j] = jugador1.diccionario['rey'][0]#poner aqui los 'objetos/fichas' del rey
        
    def crearFiguras(self, jugador, color):     
        if color == "Blanco":
            jugador.añadirDiccionario("torre", [Torre(color), Torre(color)])
            jugador.añadirDiccionario("caballo", [Caballo(color), Caballo(color)])
            jugador.añadirDiccionario("alfil", [Alfil(color), Alfil(color)])
            jugador.añadirDiccionario("rey", [Rey(color)])
            jugador.añadirDiccionario("reina", [Reina(color)])
            jugador.añadirDiccionario("peon_B", [Peon_B(),Peon_B(),Peon_B(),Peon_B(),Peon_B(),Peon_B(),Peon_B(),Peon_B()])
        elif color == "Negro":
            jugador.añadirDiccionario("torre", [Torre(color), Torre(color)])
            jugador.añadirDiccionario("caballo", [Caballo(color), Caballo(color)])
            jugador.añadirDiccionario("alfil", [Alfil(color), Alfil(color)])
            jugador.añadirDiccionario("rey", [Rey(color)])
            jugador.añadirDiccionario("reina", [Reina(color)])
            jugador.añadirDiccionario("peon_N", [Peon_N(),Peon_N(),Peon_N(),Peon_N(),Peon_N(),Peon_N(),Peon_N(),Peon_N()])
                    


    def moverFicha(self, filaInicial, columnaInicial, filaFinal, columnaFinal, jugadorNoActivo):
        coordenadasInicial = self.traducirIndice(filaInicial,columnaInicial)
        coordenadasFinal = self.traducirIndice(filaFinal,columnaFinal)
        
        if self.areaVacia(filaFinal, columnaFinal):
            figura = self.tab[coordenadasInicial[0]][coordenadasInicial[1]]
            self.tab[coordenadasFinal[0]][coordenadasFinal[1]] = figura
            self.tab[coordenadasInicial[0]][coordenadasInicial[1]] = '-'
        elif self.EsFiguraEnemiga(filaFinal, columnaFinal, jugadorNoActivo):
            if self.tab[coordenadasFinal[0]][coordenadasFinal[1]].nombre == "ReyBlanco" or self.tab[coordenadasFinal[0]][coordenadasFinal[1]].nombre == "ReyNegro":
                print(jugadorNoActivo.devolverDiccionario())
                jugadorNoActivo.diccionario.pop("rey")
                print(jugadorNoActivo.devolverDiccionario())
            figura = self.tab[coordenadasInicial[0]][coordenadasInicial[1]]
            self.tab[coordenadasFinal[0]][coordenadasFinal[1]] = figura
            self.tab[coordenadasInicial[0]][coordenadasInicial[1]] = '-'
        else:
            print("\nLa casilla está ocupada por otra pieza. Función aún en construcción.\n")

    
    def EsFiguraEnemiga(self, filaFinal, columnaFinal, jugadorNoActivo):
        coordenadas = self.traducirIndice(filaFinal,columnaFinal)
        
        figuraEsEnemiga = False
        for figura in jugadorNoActivo.diccionario.values():                  #diccionario.values() nos devuelve una lista con los valores. Debemos entrar dentro de esa lista y entonces mirar si en las listas con las figuras está la que buscamos ej: [[figura torre1, figura torre2], [figura caballo1, figura caballo 2], etc]
            if self.tab[coordenadas[0]][coordenadas[1]] in figura:
                figuraEsEnemiga = True
        return figuraEsEnemiga
    
    def EsFiguraJugadorActivo(self, filaInicial, columnaInicial, jugadorActivo):
        coordenadas = self.traducirIndice(filaInicial,columnaInicial)

        figuraEsAmiga = False
        for figura in jugadorActivo.diccionario.values():                  #diccionario.values() nos devuelve una lista con los valores. Debemos entrar dentro de esa lista y entonces mirar si en las listas con las figuras está la que buscamos ej: [[figura torre1, figura torre2], [figura caballo1, figura caballo 2], etc]
            if self.tab[coordenadas[0]][coordenadas[1]] in figura:
                figuraEsAmiga = True
        return figuraEsAmiga
    
    def seleccionarFigura(self, fila, columna):
        coordenadas = self.traducirIndice(fila,columna)
        return self.tab[coordenadas[0]][coordenadas[1]]
    

    def figuraEnCamino(self, filaInicial, columnaInicial, filaFinal, columnaFinal, figura):
        coordenadasIniciales = self.traducirIndice(filaInicial,columnaInicial)
        coordenadasFinales = self.traducirIndice(filaFinal,columnaFinal)
        caminoVacio = True

        if figura.nombre == "Peon Blanco":
                if coordenadasIniciales[0] > coordenadasFinales[0]:                                 #Ejecutamos el codigo para detectar si al moverse verticalmente hay una pieza en medio
                    print("Se realizará un movimiento vertical hacia arriba")
                    for fila in range(coordenadasIniciales[0] - coordenadasFinales[0] -1):
                        print (self.tab[coordenadasIniciales[0] - fila - 1][coordenadasIniciales[1]])
                        if self.tab[coordenadasIniciales[0] - fila - 1][coordenadasIniciales[1]] != "-":
                            caminoVacio = False

        if figura.nombre == "Peon Negro":
                if coordenadasIniciales[0] < coordenadasFinales[0]:                                 #Ejecutamos el codigo para detectar si al moverse verticalmente hay una pieza en medio
                    print("Se realizará un movimiento vertical hacia abajo")
                    for fila in range(coordenadasFinales[0] - coordenadasIniciales[0] -1):
                        print (self.tab[fila + coordenadasIniciales[0]+1][coordenadasIniciales[1]])
                        if self.tab[fila + coordenadasIniciales[0]+1][coordenadasIniciales[1]] != "-":
                            caminoVacio = False
                            
        if figura.nombre == "TorreBlanco" or figura.nombre == "TorreNegro":
                print("Se ha decidido mover una torre")
                if coordenadasIniciales[0] > coordenadasFinales[0]:                                 #Ejecutamos el codigo para detectar si al moverse verticalmente hay una pieza en medio
                    print("Se realizará un movimiento vertical hacia arriba")
                    for fila in range(coordenadasIniciales[0] - coordenadasFinales[0] -1):
                        print (self.tab[coordenadasIniciales[0] - fila - 1][coordenadasIniciales[1]])
                        if self.tab[coordenadasIniciales[0] - fila - 1][coordenadasIniciales[1]] != "-":
                            caminoVacio = False

                elif coordenadasIniciales[0] < coordenadasFinales[0]:                                 #Ejecutamos el codigo para detectar si al moverse verticalmente hay una pieza en medio
                    print("Se realizará un movimiento vertical hacia abajo")
                    for fila in range(coordenadasFinales[0] - coordenadasIniciales[0] -1):
                        print (self.tab[fila + coordenadasIniciales[0]+1][coordenadasIniciales[1]])
                        if self.tab[fila + coordenadasIniciales[0]+1][coordenadasIniciales[1]] != "-":
                            caminoVacio = False

                elif coordenadasIniciales[1] > coordenadasFinales[1]:                                 #Ejecutamos el codigo para detectar si al moverse horizontalmente hay una pieza en medio
                    print("Se realizará un movimiento horizontal hacia la izquierda")
                    for columna in range(coordenadasIniciales[1] - coordenadasFinales[1] -1):
                        print (self.tab[coordenadasIniciales[0]][coordenadasIniciales[1] - columna - 1])
                        if self.tab[coordenadasIniciales[0]][coordenadasIniciales[1] - columna - 1] != "-":
                            caminoVacio = False

                elif coordenadasIniciales[1] < coordenadasFinales[1]:                                 #Ejecutamos el codigo para detectar si al moverse horizontalmente hay una pieza en medio
                    print("Se realizará un movimiento horizontal hacia la derecha")
                    for columna in range(coordenadasFinales[1] - coordenadasIniciales[1] -1):
                        print (self.tab[coordenadasIniciales[0]][columna + coordenadasIniciales[1]+1])
                        if self.tab[coordenadasIniciales[0]][columna + coordenadasIniciales[1]+1] != "-":
                            caminoVacio = False

        if figura.nombre == "AlfilBlanco" or figura.nombre == "AlfilNegro":
                print("Se ha decidido mover un alfil")
                if (coordenadasIniciales[0] > coordenadasFinales[0]) and (coordenadasIniciales[1] > coordenadasFinales[1]):    #Ejecutamos el codigo para detectar si al moverse en diagonal (arriba, izquierda) hay una pieza en medio
                    print("Se realizará un movimiento en diagonal hacia arriba, izquierda")
                    for casilla in range(coordenadasIniciales[0] - coordenadasFinales[0] -1):
                        print (self.tab[coordenadasIniciales[0] - casilla - 1][coordenadasIniciales[1] - casilla - 1])
                        if self.tab[coordenadasIniciales[0] - casilla - 1][coordenadasIniciales[1] - casilla - 1] != "-":
                            caminoVacio = False

                elif (coordenadasIniciales[0] > coordenadasFinales[0]) and (coordenadasIniciales[1] < coordenadasFinales[1]):    #Ejecutamos el codigo para detectar si al moverse en diagonal (arriba, derecha) hay una pieza en medio
                    print("Se realizará un movimiento en diagonal hacia arriba, derecha")
                    for casilla in range(coordenadasIniciales[0] - coordenadasFinales[0] -1):
                        print (self.tab[coordenadasIniciales[0] - casilla - 1][casilla + coordenadasIniciales[1]+1])
                        if self.tab[coordenadasIniciales[0] - casilla - 1][casilla + coordenadasIniciales[1]+1] != "-":
                            caminoVacio = False

                elif (coordenadasIniciales[0] < coordenadasFinales[0]) and (coordenadasIniciales[1] < coordenadasFinales[1]):    #Ejecutamos el codigo para detectar si al moverse en diagonal (abajo, derecha) hay una pieza en medio
                    print("Se realizará un movimiento en diagonal hacia abajo, derecha")
                    for casilla in range(coordenadasFinales[0] - coordenadasIniciales[0] -1):
                        print (self.tab[casilla + coordenadasIniciales[0]+1][casilla + coordenadasIniciales[1]+1])
                        if self.tab[casilla + coordenadasIniciales[0]+1][casilla + coordenadasIniciales[1]+1] != "-":
                            caminoVacio = False

                elif (coordenadasIniciales[0] < coordenadasFinales[0]) and (coordenadasIniciales[1] > coordenadasFinales[1]):    #Ejecutamos el codigo para detectar si al moverse en diagonal (abajo, derecha) hay una pieza en medio
                    print("Se realizará un movimiento en diagonal hacia abajo, izquierda")
                    for casilla in range(coordenadasFinales[0] - coordenadasIniciales[0] -1):
                        print (self.tab[casilla + coordenadasIniciales[0]+1][coordenadasIniciales[1] - casilla - 1])
                        if self.tab[casilla + coordenadasIniciales[0]+1][coordenadasIniciales[1] - casilla - 1] != "-":
                            caminoVacio = False

        if figura.nombre == "ReinaBlanco" or figura.nombre == "ReinaNegro":
                print("Se ha decidido mover una reina")
                if (coordenadasIniciales[0] > coordenadasFinales[0]) and (coordenadasIniciales[1] == coordenadasFinales[1]):    #Ejecutamos el codigo para detectar si al moverse verticalmente hay una pieza en medio
                    print("Se realizará un movimiento vertical hacia arriba")
                    for fila in range(coordenadasIniciales[0] - coordenadasFinales[0] -1):
                        print (self.tab[coordenadasIniciales[0] - fila - 1][coordenadasIniciales[1]])
                        if self.tab[coordenadasIniciales[0] - fila - 1][coordenadasIniciales[1]] != "-":
                            caminoVacio = False

                elif (coordenadasIniciales[0] < coordenadasFinales[0]) and (coordenadasIniciales[1] == coordenadasFinales[1]):  #Ejecutamos el codigo para detectar si al moverse verticalmente hay una pieza en medio
                    print("Se realizará un movimiento vertical hacia abajo")
                    for fila in range(coordenadasFinales[0] - coordenadasIniciales[0] -1):
                        print (self.tab[fila + coordenadasIniciales[0]+1][coordenadasIniciales[1]])
                        if self.tab[fila + coordenadasIniciales[0]+1][coordenadasIniciales[1]] != "-":
                            caminoVacio = False

                elif (coordenadasIniciales[1] > coordenadasFinales[1]) and (coordenadasIniciales[0] == coordenadasFinales[0]):  #Ejecutamos el codigo para detectar si al moverse horizontalmente hay una pieza en medio
                    print("Se realizará un movimiento horizontal hacia la izquierda")
                    for columna in range(coordenadasIniciales[1] - coordenadasFinales[1] -1):
                        print (self.tab[coordenadasIniciales[0]][coordenadasIniciales[1] - columna - 1])
                        if self.tab[coordenadasIniciales[0]][coordenadasIniciales[1] - columna - 1] != "-":
                            caminoVacio = False

                elif (coordenadasIniciales[1] < coordenadasFinales[1]) and (coordenadasIniciales[0] == coordenadasFinales[0]):                                 #Ejecutamos el codigo para detectar si al moverse horizontalmente hay una pieza en medio
                    print("Se realizará un movimiento horizontal hacia la derecha")
                    for columna in range(coordenadasFinales[1] - coordenadasIniciales[1] -1):
                        print (self.tab[coordenadasIniciales[0]][columna + coordenadasIniciales[1]+1])
                        if self.tab[coordenadasIniciales[0]][columna + coordenadasIniciales[1]+1] != "-":
                            caminoVacio = False

                elif (coordenadasIniciales[0] > coordenadasFinales[0]) and (coordenadasIniciales[1] > coordenadasFinales[1]):    #Ejecutamos el codigo para detectar si al moverse en diagonal (arriba, izquierda) hay una pieza en medio
                    print("Se realizará un movimiento en diagonal hacia arriba, izquierda")
                    for casilla in range(coordenadasIniciales[0] - coordenadasFinales[0] -1):
                        print (self.tab[coordenadasIniciales[0] - casilla - 1][coordenadasIniciales[1] - casilla - 1])
                        if self.tab[coordenadasIniciales[0] - casilla - 1][coordenadasIniciales[1] - casilla - 1] != "-":
                            caminoVacio = False

                elif (coordenadasIniciales[0] > coordenadasFinales[0]) and (coordenadasIniciales[1] < coordenadasFinales[1]):    #Ejecutamos el codigo para detectar si al moverse en diagonal (arriba, derecha) hay una pieza en medio
                    print("Se realizará un movimiento en diagonal hacia arriba, derecha")
                    for casilla in range(coordenadasIniciales[0] - coordenadasFinales[0] -1):
                        print (self.tab[coordenadasIniciales[0] - casilla - 1][casilla + coordenadasIniciales[1]+1])
                        if self.tab[coordenadasIniciales[0] - casilla - 1][casilla + coordenadasIniciales[1]+1] != "-":
                            caminoVacio = False

                elif (coordenadasIniciales[0] < coordenadasFinales[0]) and (coordenadasIniciales[1] < coordenadasFinales[1]):    #Ejecutamos el codigo para detectar si al moverse en diagonal (abajo, derecha) hay una pieza en medio
                    print("Se realizará un movimiento en diagonal hacia abajo, derecha")
                    for casilla in range(coordenadasFinales[0] - coordenadasIniciales[0] -1):
                        print (self.tab[casilla + coordenadasIniciales[0]+1][casilla + coordenadasIniciales[1]+1])
                        if self.tab[casilla + coordenadasIniciales[0]+1][casilla + coordenadasIniciales[1]+1] != "-":
                            caminoVacio = False

                elif (coordenadasIniciales[0] < coordenadasFinales[0]) and (coordenadasIniciales[1] > coordenadasFinales[1]):    #Ejecutamos el codigo para detectar si al moverse en diagonal (abajo, derecha) hay una pieza en medio
                    print("Se realizará un movimiento en diagonal hacia abajo, izquierda")
                    for casilla in range(coordenadasFinales[0] - coordenadasIniciales[0] -1):
                        print (self.tab[casilla + coordenadasIniciales[0]+1][coordenadasIniciales[1] - casilla - 1])
                        if self.tab[casilla + coordenadasIniciales[0]+1][coordenadasIniciales[1] - casilla - 1] != "-":
                            caminoVacio = False


        return caminoVacio





    def cambiarJugadorActivo(self, jugador1, jugador2, jugadorActivo):
        if jugadorActivo == jugador1:
            return jugador2, jugador1
        else:
            return jugador1, jugador2
    

    def estaElReyBlancoVivo(self, jugador1):
        ReyBlancoVivo = True
        for figura in jugador1.diccionario.keys():                  #diccionario.values() nos devuelve una lista con los valores. Debemos entrar dentro de esa lista y entonces mirar si en las listas con las figuras está la que buscamos ej: [[figura torre1, figura torre2], [figura caballo1, figura caballo 2], etc]
            if "rey" in figura:
                ReyBlancoVivo = True
                return ReyBlancoVivo
            else: 
                ReyBlancoVivo = False
        return ReyBlancoVivo

    def estaElReyNegroVivo(self, jugador2):
        ReyNegroVivo = True
        for figura in jugador2.diccionario.keys():                  #diccionario.values() nos devuelve una lista con los valores. Debemos entrar dentro de esa lista y entonces mirar si en las listas con las figuras está la que buscamos ej: [[figura torre1, figura torre2], [figura caballo1, figura caballo 2], etc]
            if "rey" in figura:
                ReyNegroVivo = True
                return ReyNegroVivo
            else: 
                ReyNegroVivo = False
        return ReyNegroVivo