from Grafos.Grafo import *
from Personajes.Personaje import Personaje

__author__ = 'fredy'

# Toma un archivo con el laberinto en ASCII, imprime el inicio, el final y busca el mejor camino.
# Por ultimo escribe un archivo con formato solucion_archivo.txt en donde escribe el mejor camino encontrado.


def main():
    p = Personaje("Humano")
    p.setEarth(1)
    p.setForest(4)
    p.setMountain(0) # N/A
    p.setSand(3)
    p.setWater(2)
    p.setInicio([13,2])

    m = Personaje("Monkey")
    m.setEarth(2)
    m.setForest(1)
    m.setMountain(0) # N/A
    m.setSand(3)
    m.setWater(4)
    m.setInicio([13,4])

    o = Personaje("Octopus")
    o.setEarth(2)
    o.setForest(3)
    o.setMountain(0) # N/A
    o.setSand(0) #N/A
    o.setWater(1)
    o.setInicio([9,1])
    list = []
    list.append(p)
    list.append(m)
    list.append(o)
    name = "camino.txt"
    laberinto = leerArchivo(name)
    destinos={'K':[14,13],'T':[6,7],'P':[12,3]}
    exit ={'S':[2,14]}
    #print "inicio %s " % buscarPosicion(p.getNombre()[0],laberinto)
    #print "final %s " % buscarPosicion(destinos['T'],laberinto)
    #algoritmo = Grafo(laberinto,p.getNombre()[0],destinos['T'],p)
    for i in list:
        dest = destinos.keys()
        for d in dest:
            laberinto = leerArchivo(name)
            algoritmo = Grafo(laberinto,i.getInicio(),destinos[d],i)
            escribirSolucion(algoritmo.camino,laberinto,name,i,d)
            #el siguiente codigo es para imprimir de la K,T,P a exit
            laberinto = leerArchivo(name)
            algoritmo = Grafo(laberinto,destinos[d],exit['S'],i)
            escribirSolucionSalida(algoritmo.camino,laberinto,name,i,d,exit)
main()