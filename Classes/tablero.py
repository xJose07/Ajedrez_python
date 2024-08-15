from Classes.Figuras.Torre import Torre
from Classes.Figuras.Caballo import Caballo
from Classes.Figuras.Alfil import Alfil
from Classes.Figuras.Peon_B import Peon_B
from Classes.Figuras.Peon_N import Peon_N
from Classes.Figuras.Rey import Rey
from Classes.Figuras.Reina import Reina
from Classes.Figura import Figura
from Classes.Jugador import Jugador


class Tablero():
    def __init__(self):
        self.tab=self.crearTablero()
        self.indexf=list('ABCDEFGH')

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
        buida = True
        for i in range(x[0],y[0]+1):
            for j in range(x[1],y[1]+1):
                if self.tab[i][j][0] != '-':
                    buida = False
        return buida

    def colocarFichasInicializacion(self):
        for i in range(2):
            if i == 0:
                for j in range(8):
                    if j == 0 or j==7:
                        tor = Torre()
                        self.tab[i][j] = tor #poner aqui los 'objetos/fichas' de las torres
                    if j == 1 or j == 6:
                        cab = Caballo()
                        self.tab[i][j] = cab #poner aqui los 'objetos/fichas' de los caballos
                    if j == 2 or j == 5:
                        alf = Alfil()
                        self.tab[i][j] = alf #poner aqui los 'objetos/fichas' de los alfiles
                    if j == 3:
                        reina = Reina()
                        self.tab[i][j] = reina #poner aqui el 'objeto/ficha' de la reina
                    if j == 4:
                        rey = Rey()
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
                        tor=Torre()
                        self.tab[i][j] = tor #poner aqui los 'objetos/fichas' de las torres
                    if j == 1 or j == 6:
                        cab = Caballo()
                        self.tab[i][j] = cab #poner aqui los 'objetos/fichas' de los caballos
                    if j == 2 or j == 5:
                        alf = Alfil()
                        self.tab[i][j] = alf #poner aqui los 'objetos/fichas' de los alfiles
                    if j == 3:
                        rey = Rey()
                        self.tab[i][j] = rey #poner aqui el 'objeto/ficha' del rey
                    if j == 4:
                        reina = Reina()
                        self.tab[i][j] = reina #poner aqui el 'objeto/ficha' de la reina
        
    def crearFiguras(self):     
        jugador = Jugador()
        jugador.añadirDiccionario("torre", [Torre(), Torre()])
        jugador.añadirDiccionario("caballo", [Caballo(), Caballo()])
        jugador.añadirDiccionario("alfil", [Alfil(), Alfil()])
        jugador.añadirDiccionario("Rey", [Rey()])
        jugador.añadirDiccionario("reina", [Reina()])
        jugador.añadirDiccionario("peon_B", [Peon_B(),Peon_B(),Peon_B(),Peon_B(),Peon_B(),Peon_B(),Peon_B(),Peon_B()])
        
        #print(jugador.devolverDiccionario())
                    
                    
                    
    def moverFichas(self, fila1, columna1, fila2, columna2):
        if self.tab[fila1][columna1] == Torre:
            print("Torre seleccionada")


        if self.tab[fila1][columna1] == "X" and self.tab[fila2][columna2] != "X":
            self.tab[fila1][columna1] = "-"
            self.tab[fila2][columna2] = "X"
        else:
            print("\nMovimiento de pieza no válido.\n")
            
    #def printTorre(self):
     #   print(self.tab[0][0].hola)