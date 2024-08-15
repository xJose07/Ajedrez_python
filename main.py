from Classes.Tablero import Tablero

'''
acaba = False
while not acaba:
    try: 
        tria=int(input(missatges[lang]["tria"]))
        if tria >=0:
            nova[tria]=Crea()
            while not va.partidaAcabada():
                tau.imprimeixTauler(dev=False)
                fila = None
                while not filaOK(fila):
                    try:
                        fila = int(input("\nIntrodueix la fila 0-9: "))
                    except ValueError:
                        print("No és un dígit")
                
                col = None
                while not colOK(col):
                    col = input("Introdueix la columna A-J: ").upper()
                
                #fem el tret
                tret(nova[tria],fila,col,lang)

    except IndexError:
        pass
'''

tab = Tablero()

#tab.imprimirTablero()

tab.colocarFichasInicializacion()

tab.imprimirTablero()

#tab.moverFichas(0, 0, 1, 0)

#tab.imprimirTablero()

#tab.moverFichas(0, 7, 4, 7)

#tab.imprimirTablero()

#tab.printTorre()