import threading as thrd
import random as rd
import time
from datetime import datetime, timedelta

global maximo
global montana
global casa
global barco
global tiro
global p_montana
global p_casa
global p_barco
global p_tiro

threads = []
textzonacomun = []
textmontana = []
textcasa = []
textbarco = []
textblanco = []
textsalida = []

class Persona:

    id = 0
    nombre = "Persona"+str(id)
    eleccion = ""

    def __init__(self,id):
        self.id = id

    def eleccion(self):
        elecciones = ["montaña rusa", "casa de terror", "barco pirata", "tiro al blanco"]
        self.eleccion = rd.choice(elecciones)


def zona_comun(p):
    global textzonacomun
    sem_zona.acquire()
    juego = p.eleccion(p)
    textzonacomun.append(p.nombre+","+datetime.now().time()+","+juego+",")
    return juego


def montana_rusa(p):
    global montana
    global p_montana
    global textmontana
    while(True):
        if not lock0.locked():
            if montana == 1:
                lock0.acquire()
                montana = 0
                lock0.release()
                while(len(p_montana)>=10):
                    sem_montana.acquire()
                textmontana.append(p.nombre+","+datetime.now().time())
                p_montana.append(p)
                time.sleep(5)
                p_montana = []
                sem_montana.release()



def casa_terrorifica(p):
    global casa
    global p_casa
    global textcasa
    while(True):
        if not lock1.locked():
            if casa == 1:
                lock1.acquire()
                casa = 0
                lock1.release()
                while(len(p_casa)>=2):
                    sem_casa.acquire()
                textcasa.append(p.nombre+","+datetime.now().time())
                p_casa.append(p)
                time.sleep(3)
                p_casa = []
                sem_casa.release()    

def barco_pirata(p):
    global barco
    global p_barco
    global textbarco
    while(True):
        if not lock2.locked():
            if barco == 1:
                lock2.acquire()
                barco = 0
                lock2.release()
                while(len(p_barco)>=5):
                    sem_barco.acquire()
                textbarco.append(p.nombre+","+datetime.now().time())
                p_barco.append(p)
                time.sleep(7)
                p_barco = []
                sem_barco.release()


def tiro_al_blanco(p):
    global tiro
    global p_tiro
    global textblanco
    while(True):
        if not lock3.locked():
            if tiro == 1:
                lock3.acquire()
                tiro = 0
                lock3.release()
                while(len(p_tiro)>=1):
                    sem_tiro.acquire()
                textblanco.append(p.nombre+","+datetime.now().time())
                p_tiro.append(p)
                time.sleep(7)
                p_tiro = []
                sem_tiro.release()

def parque(p):
    juego = zona_comun(p)
    if juego == "montaña rusa":
        montana_rusa(p)

if __name__ == '__main__':

    sem_zona = thrd.BoundedSemaphore(150)
    sem_montana = thrd.BoundedSemaphore(10)
    sem_casa = thrd.BoundedSemaphore(8)
    sem_barco = thrd.BoundedSemaphore(15)
    sem_tiro = thrd.BoundedSemaphore(5)

    lock0 = thrd.Lock()
    lock1 = thrd.Lock()
    lock2 = thrd.Lock()
    lock3 = thrd.Lock()

    montana = 0
    casa = 0
    barco = 0
    tiro = 0

    p_montana = []
    p_barco = []
    p_casa = []
    p_tiro = []

    file1 = open("ZonaComun.txt","w")
    file2 = open("MontanaRusa.txt","w")
    file3 = open("CasaTerror.txt","w")
    file4 = open("BarcoPirata.txt","w")
    file5 = open("TiroBlanco.txt","w")
    file6 = open("Salida.txt","w")

    for i in textzonacomun:
        file1.write(i)
    
    for i in textmontana:
        file2.write(i)

    for i in textcasa:
        file3.write(i)

    for i in textbarco:
        file4.write(i)
    
    for i in textblanco:
        file5.write(i)
    
    for i in textsalida:
        file6.write(i)

    file1.close()
    file2.close()
    file3.close()
    file4.close()
    file5.close()
    file6.close()
