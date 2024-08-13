class Tablero():
    def __init__(self):
        self.t=self.crearTablero()

    def crearTablero(self):
        t=[]
        for i in range(8):
            fila=[]
            for j in range(8):
                fila.append('-')
            t.append(fila)  
        return t

    def imprimirTablero(self):
        INDEXF= list('ABCDEFGH')
        s =" "
        print(s,*INDEXF,end=s)
        print()
        
        for i in range(len(self.t)):
            print(i,end=s)
            for j in range(len(self.t[0])):
                print(self.t[i][j][0],end=s)
            print()

