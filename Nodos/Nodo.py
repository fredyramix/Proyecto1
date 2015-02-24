from Personajes.Personaje import Personaje


class Nodo:
    """
    pos_final : punto objetivo
    posicion : localizacion x,y del nodo
    padre : Nodo padre
    h : valor Heuristico, costo desde el nodo actual hasta el objetivo
    g : valor g, costo desde el nodo inicial hasta el nodo actual
    """
    def __init__(self, pos_final, posicion=[0, 0], padre=None, p=Personaje("pedro"), laberinto=[]):
        self.posicion = posicion
        self.padre = padre
        self.h = manhattan(self.posicion, pos_final)
        if self.padre == None:
            self.g = 0
        else:
            print laberinto[posicion[0]][posicion[1]]
            #raw_input("espera")
            if str(laberinto[posicion[0]][posicion[1]]) == str(p.getEarth()):
                self.g = self.padre.g + p.getEarth()
            elif str(laberinto[posicion[0]][posicion[1]]) == str(p.getForest()):
                self.g = self.padre.g + p.getForest()
            elif str(laberinto[posicion[0]][posicion[1]]) == str(p.getSand()):
                self.g = self.padre.g + p.getSand()
            elif str(laberinto[posicion[0]][posicion[1]]) == str(p.getWater()):
                self.g = self.padre.g + p.getWater()

        self.f = self.g + self.h

# Calcula la distancia manhattan<
def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])