from Classes.Tablero import Tablero
from Classes.Jugador import Jugador

'''
acaba = False
while not acaba:
    try: 
        tria=int(input(missatges[lang]["tria"]))
        if tria >=0:
            nova[tria]=Crea()
            while not va.partidaAcabada():
                tau.imprimeixTauler(dev=False)
                
                -----------------------------------------------------------------------------
                fila = None
                while not filaOK(fila):
                    try:
                        fila = int(input("\nIntrodueix la fila 0-7: "))
                    except ValueError:
                        print("No és un dígit")
                
                col = None
                while not colOK(col):
                    col = input("Introdueix la columna A-H: ").upper()
                
                
                -----------------------------------------------------------------------------
                #fem el tret
                tret(nova[tria],fila,col,lang)

    except IndexError:
        pass
'''


#Creamos los jugadores, y entonces creamos el tablero

jugador1 = Jugador()
jugador2 = Jugador()
tab = Tablero(jugador1, jugador2)

#Creamos las figuras y las añadimos al diccionario de cada jugador
colorW = "white"
tab.crearFiguras(jugador1, colorW)

colorB = "black"
tab.crearFiguras(jugador2, colorB)

#Colocamos las figuras en el tablero
tab.colocarFichasInicializacion(colorB, colorW, jugador1, jugador2)


finPartida = False
while finPartida == False:
    print("\nEste el el tablero de juego: \n")
    tab.imprimirTablero()
    print("\nEs el turno del jugador1, que controla las figuras blancas. Por favor, indica qué figura quieres mover.")
    columnaInicial = input("Selecciona la columna de la figura (A-H): ")
    columnaInicial = columnaInicial.upper()
    filaInicial = int(input("Ahora, selecciona la fila de la figura (0-7): "))

    #Una vez el usuario ha indicado qué figura quiere mover, hemos de comprobar que la fila y columna existen, y entonces convertimos las posiciones en coordenadas del 0-7
    
    figuraPosicionInicial = tab.traducirIndice(filaInicial,columnaInicial)
    figura = tab.seleccionarFigura(figuraPosicionInicial[0], figuraPosicionInicial[1])
    
    if tab.filaOK(filaInicial) and tab.colOK(columnaInicial) and tab.esFigura(figuraPosicionInicial[0], figuraPosicionInicial[1]):
        print(f"Se ha seleccionado la figura {figura}\n")

        tab.imprimirTablero()

        #Ahora le pedimos al usuario que seleccione la casilla donde quiere mover la figura y repetimos el proceso anterior:

        columnaFinal = input("\nSelecciona la columna donde quieres mover la figura (A-H): ")
        columnaFinal = columnaFinal.upper()
        filaFinal = int(input("Ahora, selecciona la fila donde quieres mover la figura (0-7): "))
        if tab.filaOK(filaFinal) and tab.colOK(columnaFinal):
            figuraPosicionFinal = tab.traducirIndice(filaFinal,columnaFinal)
            casillaFinal = tab.seleccionarFigura(figuraPosicionFinal[0], figuraPosicionFinal[1])
            print(f"Se ha seleccionado la figura {casillaFinal}\n")

            #Ahora sabemos qué figura quiere mover el jugador, y donde quire moverla. Hemos de comprobar que la figura pueda realizar este movimiento:
            if tab.seleccionarFigura(figuraPosicionInicial[0], figuraPosicionInicial[1]).movimientoFiguraValido(figuraPosicionInicial[0], figuraPosicionInicial[1], figuraPosicionFinal[0], figuraPosicionFinal[1], tab.EsFiguraEnemiga(figuraPosicionFinal[0], figuraPosicionFinal[1], jugador2)):
                print(f"El movimiento de la figura '{figura}' a la casilla '{casillaFinal}' es válido \n")

                #Si el movimiento es válido para la figura, entonces movemos la figura a su nueva casilla
                tab.moverFicha(figuraPosicionInicial[0], figuraPosicionInicial[1], figuraPosicionFinal[0], figuraPosicionFinal[1])
            else:
                print(f"El movimiento de la figura '{figura}' a la casilla '{casillaFinal}' no es válido!")
    else:
        print("La casilla seleccionada no contiene una figura válida.")
            
            
    



#tab.posicionFichaEnemiga(6, 0, 1, 0, jugador1, jugador2)

#Los objetos del tablero no concuerdan con los de los diccionarios de los jugadores. Al crear el tablero se deben
#usar las piezas que están en los diccionarios de los jugadores. Una vez este hecho, podremos continuar con el movimiento.



#print(tab.jugador1.devolverDiccionario())


#tab.moverFichas(0, 0, 3, 3)

#tab.imprimirTablero()

#tab.moverFichas(0, 7, 4, 7)

#tab.imprimirTablero()

#tab.printTorre()

