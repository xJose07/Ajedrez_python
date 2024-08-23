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
                        self.tab[i][j] = jugador2.diccionario['reina'][0]#poner aqui los 'objetos/fichas' de la reina
                    if j == 4:
                        self.tab[i][j] = jugador2.diccionario['rey'][0]#poner aqui los 'objetos/fichas' del rey
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
                        self.tab[i][j] = jugador1.diccionario['rey'][0]#poner aqui los 'objetos/fichas' del rey
                    if j == 4:
                        self.tab[i][j] = jugador1.diccionario['reina'][0]#poner aqui los 'objetos/fichas' de la reina
        
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

    def cambiarJugadorActivo(self, jugador1, jugador2, jugadorActivo):
        if jugadorActivo == jugador1:
            return jugador2, jugador1
        else:
            return jugador1, jugador2

