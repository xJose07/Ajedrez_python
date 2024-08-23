from Classes.Tablero import Tablero
from Classes.Jugador import Jugador

#Creamos los jugadores, y entonces creamos el tablero
colorW = "Blanco"
colorB = "Negro"

jugador1 = Jugador("jugador Blanco", colorW)
jugador2 = Jugador("jugador Negro", colorB)
tab = Tablero(jugador1, jugador2)

#Creamos las figuras y las añadimos al diccionario de cada jugador

tab.crearFiguras(jugador1, colorW)
tab.crearFiguras(jugador2, colorB)

#Colocamos las figuras en el tablero
tab.colocarFichasInicializacion(colorB, colorW, jugador1, jugador2)

jugadorActivo = jugador1
jugadorNoActivo = jugador2

finPartida = False
while not finPartida:
    print("\nEste el el tablero de juego: \n")
    tab.imprimirTablero()
    print(f"\nEs el turno del {jugadorActivo.nombre}, que controla las figuras de color {jugadorActivo.color}. Por favor, indica qué figura quieres mover: ")
   
    filaInicial = None
    while not tab.filaOK(filaInicial):
        try:
            filaInicial = int(input("Ahora, selecciona la fila de la figura (0-7): "))
        except ValueError:
            print("No es un digito")

    columnaInicial = ""
    while not tab.colOK(columnaInicial):
        columnaInicial = input("Selecciona la columna de la figura (A-H): ").upper()

    
    if not tab.areaVacia(filaInicial, columnaInicial):
        #Una vez el usuario ha indicado qué figura quiere mover, hemos de comprobar que la fila y columna existen, y entonces convertimos las posiciones en coordenadas del 0-7
        figura = tab.seleccionarFigura(filaInicial, columnaInicial)

        if tab.EsFiguraJugadorActivo(filaInicial, columnaInicial, jugadorActivo):
            print(f"\nSe ha seleccionado la figura '{figura.nombre}'\n")

            tab.imprimirTablero()

            #Ahora le pedimos al usuario que seleccione la casilla donde quiere mover la figura y repetimos el proceso anterior:
            filaFinal = None
            while not tab.filaOK(filaFinal):
                try:
                    filaFinal = int(input("Ahora, selecciona la fila donde quieres mover la figura (0-7): "))
                except ValueError:
                    print("No es un digito")
                    
            columnaFinal = ""
            while not tab.colOK(columnaFinal):
                columnaFinal = input("\nSelecciona la columna donde quieres mover la figura (A-H): ").upper()
            
                
            casillaFinal = tab.seleccionarFigura(filaFinal, columnaFinal)
            print(f"Se ha seleccionado la figura {casillaFinal}\n")
            #print(f"Se ha seleccionado la casilla (4,0) con la figura {casillaFinal.nombre}\n")

            #Ahora sabemos qué figura quiere mover el jugador, y donde quire moverla. Hemos de comprobar que la figura pueda realizar este movimiento:
            if figura.movimientoFiguraValido(filaInicial, columnaInicial, filaFinal, columnaFinal, tab.EsFiguraEnemiga(filaFinal, columnaFinal, jugadorNoActivo), tab.EsFiguraJugadorActivo(filaFinal, columnaFinal, jugadorActivo)):
                print(f"El movimiento de la figura '{figura.nombre}' a la casilla '{casillaFinal}' es válido \n")

                #Si el movimiento es válido para la figura, entonces movemos la figura a su nueva casilla y cambiamos de jugador
                tab.moverFicha(filaInicial, columnaInicial, filaFinal, columnaFinal, jugadorNoActivo)
                jugadorActivo, jugadorNoActivo = tab.cambiarJugadorActivo(jugador1, jugador2, jugadorActivo)
            else:
                print(f"El movimiento de la figura '{figura.nombre}' a la casilla '{casillaFinal}' no es válido!")
        else:
            print(f"Se ha seleccionado una figura del {jugadorNoActivo.nombre}. Por favor, selecciona una figura del {jugadorActivo.nombre}, ya que es su turno para jugar.")
    else:
        print("La casilla seleccionada no contiene una figura válida.")
            

#Bug a corregir: Caballo y Rey necesitan tener en cuenta si se mueven en casilla con figura enemiga

#Los objetos del tablero no concuerdan con los de los diccionarios de los jugadores. Al crear el tablero se deben
#usar las piezas que están en los diccionarios de los jugadores. Una vez este hecho, podremos continuar con el movimiento.



#print(tab.jugador1.devolverDiccionario())


#tab.moverFichas(0, 0, 3, 3)

#tab.imprimirTablero()

#tab.moverFichas(0, 7, 4, 7)

#tab.imprimirTablero()

#tab.printTorre()

