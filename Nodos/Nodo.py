class Nodo:
    """
    pos_final : punto objetivo
    posicion : localizacion x,y del nodo
    padre : Nodo padre
    h : valor Heuristico, costo desde el nodo actual hasta el objetivo
    g : valor g, costo desde el nodo inicial hasta el nodo actual
    """
    def __init__(self,pos_final,posicion=[0,0],padre=None):
        self.posicion = posicion
        self.padre = padre
        self.h = manhattan(self.posicion,pos_final)
        if self.padre == None:
            self.g = 0
        else:
            self.g = self.padre.g + 1
        self.f = self.g + self.h

#Calcula la distancia manhattan
def manhattan(a,b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])