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
    #list.append(o)
    name = "camino.txt"
    laberinto = leerArchivo(name)
    destinos={'K':[14,13],'T':[6,7],'P':[12,3]}
    #exit 'S':[2,14]
    #print "inicio %s " % buscarPosicion(p.getNombre()[0],laberinto)
    #print "final %s " % buscarPosicion(destinos['T'],laberinto)

    #algoritmo = Grafo(laberinto,p.getNombre()[0],destinos['T'],p)
    for i in list:
            laberinto = leerArchivo(name)
            algoritmo1 = Grafo(laberinto,i.getInicio(),destinos['T'],i)
            escribirSolucion(algoritmo1.camino,laberinto,name,i,'T')

            laberinto = leerArchivo(name)

            algoritmo2 = Grafo(laberinto,i.getInicio(),destinos['K'],i)
            escribirSolucion(algoritmo2.camino,laberinto,name,i,'K')

            laberinto = leerArchivo(name)

            algoritmo3 = Grafo(laberinto,i.getInicio(),destinos['P'],i)
            escribirSolucion(algoritmo3.camino,laberinto,name,i,'P')
            laberinto = leerArchivo(name)

main()