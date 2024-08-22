#jugador = {"torres": [object,object], "alfil":[object,object]}

class Jugador():
    def __init__(self, nombre, color):
        self.diccionario={}
        self.nombre = nombre
        self.color = color
        
    def añadirDiccionario(self, tipo, figura):
        if tipo in self.diccionario:
            self.diccionario.update({tipo:figura})
        else:
            self.diccionario[tipo] = figura
        
    def devolverDiccionario(self):
        return self.diccionario.items()
