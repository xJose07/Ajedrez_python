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


reyBlanco = True
reyNegro = True
while reyBlanco and reyNegro:
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
            if figura.movimientoFiguraValido(filaInicial, columnaInicial, filaFinal, columnaFinal, tab.EsFiguraEnemiga(filaFinal, columnaFinal, jugadorNoActivo), tab.EsFiguraJugadorActivo(filaFinal, columnaFinal, jugadorActivo)) and tab.figuraEnCamino(filaInicial, columnaInicial, filaFinal, columnaFinal, figura):
                print(f"El movimiento de la figura '{figura.nombre}' a la casilla '{casillaFinal}' es válido \n")

                #Aquí haremos el movimiento "enroque". En el objeto "Rey" revisamos si es el primer movimiento. Entonces hemos de revisar si la torre
                #del lado donde se hace el movimiento se ha movido, y si el camino entre el rey y la torre está libre. Entonces haríamos el movimiento
                #Para el Rey Blanco hemos de hacer las comprovaciones cuando se mueve a la casilla C7 o G7. 
                #Para el Rey Blanco hemos de hacer las comprovaciones cuando se mueve a la casilla B0 o F0.
                #Primero miraremos el jugador que está activo y si se ha seleccionado el rey. Entonces revisamos si se quiere realizar un movimiento
                #lateral de 2 casillas

                if figura.nombre == "ReyBlanco" and (columnaInicial.upper() == "E" and columnaFinal.upper() == "G" or columnaInicial.upper() == "E" and columnaFinal.upper() == "C"):
                    #Ahora hemos de ver a qué lado del tablero se quiere realizar el movimiento,
                    if columnaInicial.upper() == "E" and columnaFinal.upper() == "G":
                        #Si el movimiento es +2, entonces se debe revisar que las casillas F7 y G7 están vacías, y que la torre en H7 no se ha movido aún
                        casillaF7 = tab.seleccionarFigura(7, "F")
                        casillaG7 = tab.seleccionarFigura(7, "G")
                        casillaH7 = tab.seleccionarFigura(7, "H")
                        if casillaF7 == "-" and casillaG7 == "-" and casillaH7.nombre == "TorreBlanco":
                            if casillaH7.primerMovimiento == True:
                                #Ahora moveríamos el rey a G7
                                tab.moverFicha(filaInicial, columnaInicial, filaFinal, columnaFinal, jugadorNoActivo)
                                #Ahora movemos la torre a F7
                                tab.moverFicha(7, "H", 7, "F", jugadorNoActivo)
                    elif columnaInicial.upper() == "E" and columnaFinal.upper() == "C":
                        #Si el movimiento es -2, entonces se debe revisar que las casillas D7, C7 y B7 están vacías, y que la torre en A7 no se ha movido aún
                        casillaD7 = tab.seleccionarFigura(7, "D")
                        casillaC7 = tab.seleccionarFigura(7, "C")
                        casillaB7 = tab.seleccionarFigura(7, "B")
                        casillaA7 = tab.seleccionarFigura(7, "A")
                        if casillaD7 == "-" and casillaC7 == "-" and casillaB7 == "-" and casillaA7.nombre == "TorreBlanco":
                            if casillaA7.primerMovimiento == True:
                                #Ahora moveríamos el rey a C7
                                tab.moverFicha(filaInicial, columnaInicial, filaFinal, columnaFinal, jugadorNoActivo)
                                #Ahora movemos la torre a D7
                                tab.moverFicha(7, "A", 7, "D", jugadorNoActivo)
                            
                        
                if figura.nombre == "ReyNegro" and (columnaInicial.upper() == "D" and columnaFinal.upper() == "B" or columnaInicial.upper() == "D" and columnaFinal.upper() == "F"):
                    #Ahora hemos de ver a qué lado del tablero se quiere realizar el movimiento,
                    if columnaInicial.upper() == "D" and columnaFinal.upper() == "B":
                        #Si el movimiento es +2, entonces se debe revisar que las casillas B0 y C0 están vacías, y que la torre en A7 no se ha movido aún
                        casillaC0 = tab.seleccionarFigura(0, "C")
                        casillaB0 = tab.seleccionarFigura(0, "B")
                        casillaA0 = tab.seleccionarFigura(0, "A")
                        if casillaC0 == "-" and casillaB0 == "-" and casillaA0.nombre == "TorreNegro":
                            if casillaA0.primerMovimiento == True:
                                #Ahora moveríamos el rey a B0
                                tab.moverFicha(filaInicial, columnaInicial, filaFinal, columnaFinal, jugadorNoActivo)
                                #Ahora movemos la torre a C0
                                tab.moverFicha(0, "A", 0, "C", jugadorNoActivo)
                    elif columnaInicial.upper() == "D" and columnaFinal.upper() == "F":
                        #Si el movimiento es -2, entonces se debe revisar que las casillas E0, F0 y G0 están vacías, y que la torre en H0 no se ha movido aún
                        casillaE0 = tab.seleccionarFigura(0, "E")
                        casillaF0 = tab.seleccionarFigura(0, "F")
                        casillaG0 = tab.seleccionarFigura(0, "G")
                        casillaH0 = tab.seleccionarFigura(0, "H")
                        if casillaE0 == "-" and casillaF0 == "-" and casillaG0 == "-" and casillaH0.nombre == "TorreNegro":
                            if casillaH0.primerMovimiento == True:
                                #Ahora moveríamos el rey a F0
                                tab.moverFicha(filaInicial, columnaInicial, filaFinal, columnaFinal, jugadorNoActivo)
                                #Ahora movemos la torre a E0
                                tab.moverFicha(0, "H", 0, "E", jugadorNoActivo) 
                    
                else:
                    #En este caso no hay enroque. Si el movimiento es válido para la figura, entonces movemos la figura a su nueva casilla
                    tab.moverFicha(filaInicial, columnaInicial, filaFinal, columnaFinal, jugadorNoActivo)
                #Revisamos si uno de los reyes ha muerto, y si no es así cambiamos de jugador
                if tab.estaElReyBlancoVivo(jugador1) is False:
                    print("¡El rey blanco ha muerto, la partida ha terminado, y el jugador negro gana!")
                    reyBlanco = False
                if tab.estaElReyNegroVivo(jugador2) is False:
                    print("¡El rey negro ha muerto, la partida ha terminado, y el jugador blanco gana!")
                    reyNegro = False
                    
                jugadorActivo, jugadorNoActivo = tab.cambiarJugadorActivo(jugador1, jugador2, jugadorActivo)
            else:
                print(f"El movimiento de la figura '{figura.nombre}' a la casilla '{casillaFinal}' no es válido!")
        else:
            print(f"Se ha seleccionado una figura del {jugadorNoActivo.nombre}. Por favor, selecciona una figura del {jugadorActivo.nombre}, ya que es su turno para jugar.")
    else:
        print("La casilla seleccionada no contiene una figura válida.")
            





