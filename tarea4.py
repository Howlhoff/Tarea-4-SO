import threading
import random
import time

global maximo

class Juegos:

    fila = 0
    duracion = 0
    capacidad = 0

    def tiro_al_blanco(self):
        self.fila = 5
        self.duracion = 7
        self.capacidad = 1


    def barco_pirata(self):
        self.fila = 15
        self.duracion = 7
        self.capacidad = 5


    def casa_terrorifica(self):
        self.fila = 8
        self.duracion = 3
        self.capacidad = 2


    def montana_rusa(self):
        self.fila = 10
        self.duracion = 5
        self.capacidad = 10

