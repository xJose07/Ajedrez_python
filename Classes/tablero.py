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
    
    def filaOK(f):
        return f in range(8)

    def colOK(self, col):
        if len(col) == 1:
            return col in self.indexf
        else:
            return False
       
    #Comprobar si la casilla está vacia (al colocar las figuras despues del input del usuario)
    def areaVacia(self,x,y):
        buida = False
        for i in range(x[0],y[0]+1):
            for j in range(x[1],y[1]+1):
                if self.tab[i][j][0] == '-':
                    buida = True
        return buida

    def areaVacia2(self,x,y):
        buida = False
        if self.tab[x][y] == '-':
            buida = True
        return buida
    
    def colocarFichasInicializacion(self, color1, color2):
        for i in range(2):
            if i == 0:
                for j in range(8):
                    if j == 0 or j==7:
                        tor = Torre(color1)
                        self.tab[i][j] = tor #poner aqui los 'objetos/fichas' de las torres
                    if j == 1 or j == 6:
                        cab = Caballo(color1)
                        self.tab[i][j] = cab #poner aqui los 'objetos/fichas' de los caballos
                    if j == 2 or j == 5:
                        alf = Alfil(color1)
                        self.tab[i][j] = alf #poner aqui los 'objetos/fichas' de los alfiles
                    if j == 3:
                        reina = Reina(color1)
                        self.tab[i][j] = reina #poner aqui el 'objeto/ficha' de la reina
                    if j == 4:
                        rey = Rey(color1)
                        self.tab[i][j] = rey #poner aqui el 'objeto/ficha' del rey
            if i == 1:
                for j in range(8):
                    peon_N = Peon_N()
                    self.tab[i][j] = peon_N #poner aqui los 'objetos/fichas' de los peones negros
        for i in range(6, 8):
            if i == 6:
                for j in range(8):
                    peon_B = Peon_B()
                    self.tab[i][j] = peon_B #poner aqui los 'objetos/fichas' de los peones blancos
            if i == 7:
                for j in range(8):
                    if j == 0 or j==7:
                        tor=Torre(color2)
                        self.tab[i][j] = tor #poner aqui los 'objetos/fichas' de las torres
                    if j == 1 or j == 6:
                        cab = Caballo(color2)
                        self.tab[i][j] = cab #poner aqui los 'objetos/fichas' de los caballos
                    if j == 2 or j == 5:
                        alf = Alfil(color2)
                        self.tab[i][j] = alf #poner aqui los 'objetos/fichas' de los alfiles
                    if j == 3:
                        rey = Rey(color2)
                        self.tab[i][j] = rey #poner aqui el 'objeto/ficha' del rey
                    if j == 4:
                        reina = Reina(color2)
                        self.tab[i][j] = reina #poner aqui el 'objeto/ficha' de la reina
        
    def crearFiguras(self, jugador, color):     
        if color == "white":
            jugador.añadirDiccionario("torre", [Torre(color), Torre(color)])
            jugador.añadirDiccionario("caballo", [Caballo(color), Caballo(color)])
            jugador.añadirDiccionario("alfil", [Alfil(color), Alfil(color)])
            jugador.añadirDiccionario("Rey", [Rey(color)])
            jugador.añadirDiccionario("reina", [Reina(color)])
            jugador.añadirDiccionario("peon_B", [Peon_B(),Peon_B(),Peon_B(),Peon_B(),Peon_B(),Peon_B(),Peon_B(),Peon_B()])
        elif color == "black":
            jugador.añadirDiccionario("torre", [Torre(color), Torre(color)])
            jugador.añadirDiccionario("caballo", [Caballo(color), Caballo(color)])
            jugador.añadirDiccionario("alfil", [Alfil(color), Alfil(color)])
            jugador.añadirDiccionario("Rey", [Rey(color)])
            jugador.añadirDiccionario("reina", [Reina(color)])
            jugador.añadirDiccionario("peon_N", [Peon_N(),Peon_N(),Peon_N(),Peon_N(),Peon_N(),Peon_N(),Peon_N(),Peon_N()])
                    


    def moverFicha(self, filaInicial, columnaInicial):
        movimientoFigura = self.tab[filaInicial][columnaInicial].movimiento()
        filaFinal = filaInicial + movimientoFigura[0]
        columnaFinal = columnaInicial + movimientoFigura[1]
        if self.areaVacia2(filaFinal, columnaFinal):
            print(f"\nSe ha seleccionado {self.tab[filaInicial][columnaInicial].nombre}\n")
            figura = self.tab[filaInicial][columnaInicial]
            self.tab[filaFinal][columnaFinal] = figura
            self.tab[filaInicial][columnaInicial] = '-'
        else:
            print("\nMovimiento de pieza no válido.\n")


    def posicionFichaEnemiga(self, filaInicial, columnaInicial, filaFinal, columnaFinal, jugador1, jugador2):
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
            print(jugador1.diccionario.values())
            print("\n")
            print(jugador2.diccionario.values())
            print(self.tab[filaInicial][columnaInicial])
            print(self.tab[filaInicial][columnaInicial+1])
            print(self.tab[filaInicial][columnaInicial+2])
            print(self.tab[filaInicial][columnaInicial+3])
            print(self.tab[filaInicial][columnaInicial+4])
            print(self.tab[filaInicial][columnaInicial+5])
            print(self.tab[filaInicial][columnaInicial+6])
            print(self.tab[filaInicial][columnaInicial+7])