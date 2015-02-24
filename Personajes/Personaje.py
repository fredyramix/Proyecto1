# -*- encoding: utf-8 -*-
# clase Personaje
__author__ = 'fredy'

costo = 0


class Personaje(object):
    def __init__(self, nombre):
        #constructor
        self.nombre = nombre
        self.water = costo
        self.sand = costo
        self.forest = costo
        self.earth = costo
        self.mountain = costo
        self.inicio=[]

    def __str__(self):
        p = "Nombre: " + self.nombre + "\nMountain: " + str(self.mountain)+  "\nEarth: " + str(self.earth) +"\nWater: " + str(self.water) + "\nSand: " + str(
        self.sand) + "\nForest: " + str(self.forest)
        return p

    def getInicio(self):
        return self.inicio


    def setInicio(self, x):
        self.inicio = x




    def getNombre(self):
        return self.nombre


    def setNombre(self, n):
        self.nombre = n


    def getWater(self):
        return self.water


    def setWater(self, w):
        self.water = w


    def getSand(self):
        return self.sand


    def setSand(self, s):
        self.sand = s


    def getForest(self):
        return self.forest


    def setForest(self, f):
        self.forest = f


    def getEarth(self):
        return self.earth


    def setEarth(self, e):
        self.earth = e


    def getMountain(self):
        return self.mountain


    def setMountain(self, m):
        self.mountain = m