import threading
import random
import time
from datetime import datetime


global f_ZonaComun
global f_MontanaRusa
global f_CasaTerror
global f_BarcoPirata
global f_TiroBlanco
global f_Salida

global textZonaComun

global MontanaRusa
global CasaTerror
global BarcoPirata
global TiroBlanco

class Juego:
    nombre = ""
    capacidadFila = 0
    duracion = 0
    capacidadJuego = 0
    lock = threading.Lock()
    fila = 0 # cantidad de personas en la fila actualmente

    def __init__(self,nombre,capacidadFila,duracion,capacidadJuego):
        self.nombre = nombre
        self.capacidadFila = capacidadFila
        self.duracion = duracion
        self.capacidadJuego = capacidadJuego


    def jugar(self,p,time_in):
        s_juego = threading.BoundedSemaphore(self.capacidadJuego)

        s_juego.acquire()
        self.fila += 1

        while (True):
            if self.fila >= self.capacidadJuego:
                break
        
        self.lock.acquire()
        self.log(p.nombre+", "+time_in+", "+datetime.now().strftime("%H:%M:%S")+"\n")
        self.lock.release()
        time.sleep(self.duracion)
        self.fila -= self.capacidadJuego
    
    def log(self, string):
        global f_MontanaRusa
        global f_CasaTerror
        global f_BarcoPirata
        global f_TiroBlanco

        if self.nombre == "Montaña Rusa":
            f_MontanaRusa = open("MontañaRusa.txt","a")
            f_MontanaRusa.write(string)
            f_MontanaRusa.close()
        elif self.nombre == "Casa del Terror":
            f_CasaTerror = open("CasaTerror.txt","a")
            f_CasaTerror.write(string)
            f_CasaTerror.close()
        elif self.nombre == "Barco Pirata":
            f_BarcoPirata = open("BarcoPirata.txt","a")
            f_BarcoPirata.write(string)
            f_BarcoPirata.close()
        elif self.nombre == "Tiro al Blanco":
            f_TiroBlanco = open("TiroBlanco.txt","a")
            f_TiroBlanco.write(string)
            f_TiroBlanco.close()
        else:
            print("Error de nombre de juego.\n")



class Persona:
    id = 0
    nombre = ""

    def __init__(self,id):
        self.id = id
        self.nombre = "Persona_"+str(id)

def t_persona(i):
    global f_ZonaComun
    global f_Salida

    global textZonaComun

    global MontanaRusa
    global CasaTerror
    global BarcoPirata
    global TiroBlanco

    s_FilaMR = threading.BoundedSemaphore(MontanaRusa.capacidadFila)
    s_FilaCT = threading.BoundedSemaphore(CasaTerror.capacidadFila)
    s_FilaBP = threading.BoundedSemaphore(BarcoPirata.capacidadFila)
    s_FilaTB = threading.BoundedSemaphore(TiroBlanco.capacidadFila)

    p = Persona(i+1)
    time_in = ""

    # Persona esta en la zona comun
    lockZC.acquire()
    f_ZonaComun = open("ZonaComun.txt","a")
    eleccion = random.choice(juegos) # Persona elige un juego
    textZonaComun[i] = p.nombre+", "+datetime.now().strftime("%H:%M:%S")+", "+eleccion+", "

    # Persona en juego
    if eleccion == "Montaña Rusa":
        # Guardar log de Zona Comun
        s_FilaMR.acquire()
        time_in = datetime.now().strftime("%H:%M:%S")
        textZonaComun[i] += time_in + "\n"
        f_ZonaComun.write(textZonaComun[i])
        f_ZonaComun.close()
        lockZC.release()
        
        # Juego
        
        MontanaRusa.jugar(p,time_in)
        s_FilaMR.release()
    elif eleccion == "Casa del Terror":
        # Guardar log de Zona Comun
        s_FilaCT.acquire()
        time_in = datetime.now().strftime("%H:%M:%S")
        textZonaComun[i] += time_in + "\n"
        f_ZonaComun.write(textZonaComun[i])
        f_ZonaComun.close()
        lockZC.release()
        
        #Juego
        CasaTerror.jugar(p,time_in)
        s_FilaCT.release()
    elif eleccion == "Barco Pirata":
        # Guardar log de Zona Comun
        s_FilaBP.acquire()
        time_in = datetime.now().strftime("%H:%M:%S")
        textZonaComun[i] += time_in + "\n"
        f_ZonaComun.write(textZonaComun[i])
        f_ZonaComun.close()
        lockZC.release()
        
        # Juego
        BarcoPirata.jugar(p,time_in)
        s_FilaBP.release()
    elif eleccion == "Tiro al Blanco":
        # Guardar log de Zona Comun
        s_FilaTB.acquire()
        time_in = datetime.now().strftime("%H:%M:%S")
        textZonaComun[i] += time_in + "\n"
        f_ZonaComun.write(textZonaComun[i])
        f_ZonaComun.close()
        lockZC.release()

        # Juego
        TiroBlanco.jugar(p,time_in)
        s_FilaTB.release()
    # Persona termina el juego

    # Persona sale del parque
    lockS.acquire()
    f_Salida = open("Salida.txt","a")
    f_Salida.writelines(p.nombre+", "+datetime.now().strftime("%H:%M:%S")+"\n")
    f_Salida.close()
    lockS.release()




#------------"MAIN"------------#
f_ZonaComun = open("ZonaComun.txt","w")
f_MontanaRusa = open("MontañaRusa.txt","w")
f_CasaTerror = open("CasaTerror.txt","w")
f_BarcoPirata = open("BarcoPirata.txt","w")
f_TiroBlanco = open("TiroBlanco.txt","w")
f_Salida = open("Salida.txt","w")

f_ZonaComun.close()
f_TiroBlanco.close()
f_MontanaRusa.close()
f_CasaTerror.close()
f_BarcoPirata.close()
f_Salida.close()

MontanaRusa = Juego("Montaña Rusa", 10, 5, 10)
CasaTerror = Juego("Casa del Terror", 8, 3, 2)
BarcoPirata = Juego("Barco Pirata", 15, 7, 5)
TiroBlanco = Juego("Tiro al Blanco", 5, 2, 1)

lockZC = threading.Lock()
lockS = threading.Lock()


juegos = ["Montaña Rusa","Casa del Terror","Barco Pirata","Tiro al Blanco"]

textZonaComun = list(range(150))

threads = []

for i in range(150):
    threads.append(threading.Thread(target=t_persona, args=(i,), daemon=True))

for t in threads:
    t.start()

for t in threads:
    t.join()

