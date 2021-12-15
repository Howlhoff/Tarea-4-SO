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
        return self.eleccion


def zona_comun(p):
    global textzonacomun
    sem_zona.acquire()
    juego = p.eleccion()
    textzonacomun.append(p.nombre+", "+datetime.now().time()+", "+juego+", ")
    return juego


def montana_rusa(p):
    t_fila = datetime.now().strftime("%H:%M:%S")

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
                textmontana.append(p.nombre+", "+t_fila+", "+datetime.now().time())
                p_montana.append(p)
                time.sleep(5)
                p_montana = []
                sem_montana.release()
                return 1



def casa_terrorifica(p):
    t_fila = datetime.now().strftime("%H:%M:%S")

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
                textcasa.append(p.nombre+", "+t_fila+", "+datetime.now().time())
                p_casa.append(p)
                time.sleep(3)
                p_casa = []
                sem_casa.release()    
                return 1

def barco_pirata(p):
    t_fila = datetime.now().strftime("%H:%M:%S")

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
                textbarco.append(p.nombre+", "+t_fila+", "+datetime.now().time())
                p_barco.append(p)
                time.sleep(7)
                p_barco = []
                sem_barco.release()
                return 1


def tiro_al_blanco(p):
    t_fila = datetime.now().strftime("%H:%M:%S")
    
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
                textblanco.append(p.nombre+", "+t_fila+", "+datetime.now().time())
                p_tiro.append(p)
                time.sleep(7)
                p_tiro = []
                sem_tiro.release()
                return 1

def parque(i):
    t_juego = datetime.now().strftime("%H:%M:%S")
    global textzonacomun
    global textsalida
    p = Persona(i+1)
    lockC.acquire()
    juego = zona_comun(p)
    if juego == "montaña rusa":
        textzonacomun[i] += t_juego
        lockC.release()
        montana_rusa(p)
    elif juego == "casa de terror":
        textzonacomun[i] += t_juego
        lockC.release()
        casa_terrorifica(p)
    elif juego == "barco pirata":
        textzonacomun[i] += t_juego
        lockC.release()
        barco_pirata(p)
    else:
        textzonacomun[i] += t_juego
        lockC.release()
        tiro_al_blanco(p)

    textsalida.append(p.nombre+", "+datetime.now().time())
    return 1
    
    
    

if __name__ == '__main__':

    for i in range(150):
        threads.append(thrd.Thread(target=parque, args=(i,)))


    sem_zona = thrd.BoundedSemaphore(150)
    sem_montana = thrd.BoundedSemaphore(10)
    sem_casa = thrd.BoundedSemaphore(8)
    sem_barco = thrd.BoundedSemaphore(15)
    sem_tiro = thrd.BoundedSemaphore(5)

    lock0 = thrd.Lock()
    lock1 = thrd.Lock()
    lock2 = thrd.Lock()
    lock3 = thrd.Lock()
    lockC = thrd.Lock()

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
