from Grafos.Grafo import *
__author__ = 'fredy'
import sys

# Toma un archivo con el laberinto en ASCII, imprime el inicio, el final y busca el mejor camino.
# Por ultimo escribe un archivo con formato solucion_archivo.txt en donde escribe el mejor camino encontrado.
def main():
    name = "camino.txt"
    laberinto = leerArchivo(name)
    print "inicio %s " % buscarPosicion('I',laberinto)
    print "final %s " % buscarPosicion('F',laberinto)
    algoritmo = Grafo(laberinto)
    escribirSolucion(algoritmo.camino,laberinto,name)

main()