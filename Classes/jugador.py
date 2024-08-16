#jugador = {"torres": [object,object], "alfil":[object,object]}

class Jugador():
    def __init__(self):
        self.diccionario={}
        
    def añadirDiccionario(self, tipo, figura):
        if tipo in self.diccionario:
            self.diccionario.update({tipo:figura})
        else:
            self.diccionario[tipo] = figura
        
    def devolverDiccionario(self):
        return self.diccionario.items()
