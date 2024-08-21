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
                #if type(self.tab[i][j]) == Torre or type(self.tab[i][j]) == Alfil or type(self.tab[i][j]) == Caballo or type(self.tab[i][j])==Reina or type(self.tab[i][j])==Rey or type(self.tab[i][j])==Peon_N or type(self.tab[i][j])==Peon_B:
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
        buida = False
        if self.tab[x][y] == '-':
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
        if color == "white":
            jugador.añadirDiccionario("torre", [Torre(color), Torre(color)])
            jugador.añadirDiccionario("caballo", [Caballo(color), Caballo(color)])
            jugador.añadirDiccionario("alfil", [Alfil(color), Alfil(color)])
            jugador.añadirDiccionario("rey", [Rey(color)])
            jugador.añadirDiccionario("reina", [Reina(color)])
            jugador.añadirDiccionario("peon_B", [Peon_B(),Peon_B(),Peon_B(),Peon_B(),Peon_B(),Peon_B(),Peon_B(),Peon_B()])
        elif color == "black":
            jugador.añadirDiccionario("torre", [Torre(color), Torre(color)])
            jugador.añadirDiccionario("caballo", [Caballo(color), Caballo(color)])
            jugador.añadirDiccionario("alfil", [Alfil(color), Alfil(color)])
            jugador.añadirDiccionario("rey", [Rey(color)])
            jugador.añadirDiccionario("reina", [Reina(color)])
            jugador.añadirDiccionario("peon_N", [Peon_N(),Peon_N(),Peon_N(),Peon_N(),Peon_N(),Peon_N(),Peon_N(),Peon_N()])
                    


    def moverFicha(self, filaInicial, columnaInicial, filaFinal, columnaFinal):
        if self.areaVacia(filaFinal, columnaFinal):
            figura = self.tab[filaInicial][columnaInicial]
            self.tab[filaFinal][columnaFinal] = figura
            self.tab[filaInicial][columnaInicial] = '-'
        else:
            print("\nLa casilla está ocupada por otra pieza. Función aún en construcción.\n")

    def esFigura(self, filaInicial, columnaInicial):
        esUnaFigura = True
        if self.tab[filaInicial][columnaInicial] == '-':
            esUnaFigura = False
        return esUnaFigura
    
    def EsFiguraEnemiga(self, filaFinal, columnaFinal, jugadorNoActivo):
        figuraEsEnemiga = False
        for figura in jugadorNoActivo.diccionario.values():                  #diccionario.values() nos devuelve una lista con los valores. Debemos entrar dentro de esa lista y entonces mirar si en las listas con las figuras está la que buscamos ej: [[figura torre1, figura torre2], [figura caballo1, figura caballo 2], etc]
            if self.tab[filaFinal][columnaFinal] in figura:
                figuraEsEnemiga = True
        return figuraEsEnemiga
    
    def posicionFichaEnemiga(self, filaInicial, columnaInicial, filaFinal, columnaFinal, jugador1, jugador2):
        for figura in jugador1.diccionario.values():                  #diccionario.values() nos devuelve una lista con los valores. Debemos entrar dentro de esa lista y entonces mirar si en las listas con las figuras está la que buscamos ej: [[figura torre1, figura torre2], [figura caballo1, figura caballo 2], etc]
            if self.tab[filaInicial][columnaInicial] in figura:
                print("La figura seleccionada pertenece al jugador1")
        if self.tab[filaInicial][columnaInicial] in jugador1.diccionario.values() and self.tab[filaInicial][columnaInicial] != '-':
            print("La figura seleccionada pertenece al jugador1")
            if self.tab[filaFinal][columnaFinal] not in jugador1.diccionario.values() and self.tab[filaFinal][columnaFinal] != '-':
                print("El jugador ha movido su figura a una casilla con una figura enemiga")
            elif self.tab[filaFinal][columnaFinal] == '-':
                print("El jugador ha movido su figura a una casilla vacía")
            else:
                print("El jugador ha movido su figura a una casilla con una figura própia. Movimiento no válido")

        elif self.tab[filaInicial][columnaInicial] in jugador2.diccionario.values() and self.tab[filaInicial][columnaInicial] != '-':
            print("La figura seleccionada pertenece al jugador2")
        elif self.tab[filaInicial][columnaInicial] == '-':
            print("Se ha seleccionado una casilla vacía")

        else:
            print("La figura seleccionada pertenece al jugador enemigo")

    def seleccionarFigura(self, fila, columna):
        return self.tab[fila][columna]
