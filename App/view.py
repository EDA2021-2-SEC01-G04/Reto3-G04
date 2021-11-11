"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Avistamientos en una ciudad")
    print("3- Avistamientos por duración")
    print("4- Avistamientos por Hora/Minutos del día")
    print("5- Avistamientos en un rango de fechas")
    print("6- Avistamientos de una Zona Geográfica")

catalog = None

def getufosRangeTime(analyzer,time1,time2):
    return controller.getufosRangeTime(analyzer,time1,time2)


def getufosRangeDate(analyzer,time1,time2):
    return controller.getufosRangeDate(analyzer,time1,time2)


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = controller.init()
        time = controller.loadArtists(catalog)
        print("El tiempo de carga de datos fue de: "+str(time))
        print("El totalde avistamients cargados fue de: " + str(lt.size(catalog["ufos"])))
        

    elif int(inputs[0]) == 2:
        city = input("Ingrese el nombre de la ciudad\n")
        lst = controller.getUfosByCity(catalog,city)
        size = lt.size(lst)
        if lst is str:
            print(lst)
        else:
            print("El total de avistamiento en " + city + "fue de: " + str(size))
            print("---------------------------------------------------")
            print("Fecha: " +lt.getElement(lst,1)["datetime"]," Ciudad: " + lt.getElement(lst,1)["city"]," Estado: "+ lt.getElement(lst,1)["state"] ," País: " + lt.getElement(lst,1)["country"]," Duracion: " + lt.getElement(lst,1)["duration (seconds)"]," Forma: " + lt.getElement(lst,1)["shape"])
            print("---------------------------------------------------")
            print("Fecha: " +lt.getElement(lst,2)["datetime"]," Ciudad: " + lt.getElement(lst,2)["city"]," Estado: "+ lt.getElement(lst,2)["state"] ," País: " + lt.getElement(lst,2)["country"]," Duracion: " + lt.getElement(lst,2)["duration (seconds)"]," Forma: " + lt.getElement(lst,2)["shape"])
            print("---------------------------------------------------")
            print("Fecha: " +lt.getElement(lst,3)["datetime"]," Ciudad: " + lt.getElement(lst,3)["city"]," Estado: "+ lt.getElement(lst,3)["state"] ," País: " + lt.getElement(lst,3)["country"]," Duracion: " + lt.getElement(lst,3)["duration (seconds)"]," Forma: " + lt.getElement(lst,3)["shape"])
            print("---------------------------------------------------")
            print("Fecha: " +lt.getElement(lst,size)["datetime"]," Ciudad: " + lt.getElement(lst,size)["city"]," Estado: "+ lt.getElement(lst,size)["state"] ," País: " + lt.getElement(lst,size)["country"]," Duracion: " + lt.getElement(lst,size)["duration (seconds)"]," Forma: " + lt.getElement(lst,size)["shape"])
            print("---------------------------------------------------")
            print("Fecha: " +lt.getElement(lst,size-1)["datetime"]," Ciudad: " + lt.getElement(lst,size-1)["city"]," Estado: "+ lt.getElement(lst,size-1)["state"] ," País: " + lt.getElement(lst,size-1)["country"]," Duracion: " + lt.getElement(lst,size-1)["duration (seconds)"]," Forma: " + lt.getElement(lst,size-1)["shape"])
            print("---------------------------------------------------")
            print("Fecha: " +lt.getElement(lst,size-2)["datetime"]," Ciudad: " + lt.getElement(lst,size-2)["city"]," Estado: "+ lt.getElement(lst,size-2)["state"] ," País: " + lt.getElement(lst,size-2)["country"]," Duracion: " + lt.getElement(lst,size-2)["duration (seconds)"]," Forma: " + lt.getElement(lst,size-2)["shape"])

    elif int(inputs[0]) == 3:
        min = int(input("Ingrese el limite inferior en segundos: "))
        max = int(input("Ingrese el limite superior en segundos: "))
        resultado = controller.sightings(catalog,min,max)
        print("De los avistamientos en ese intervalo de segundos, el mayor es: " + str(resultado[0]) + " con un total de: " + str(resultado[1]) + " apariciones")
        print("Los siguientes son los primeros 3 y ultimos 3 avistamientos en el rango: ")
        print("Fecha: " + str(resultado[8]["datetime"]) + ", Ciudad: " + str(resultado[8]["city"]) + ", Pais: " + str(resultado[8]["country"]) + ", duracion en segundos: " + str(resultado[8]["duration (seconds)"]) + ", Forma del objeto: " + str(resultado[8]["shape"]))
        print("Fecha: " + str(resultado[7]["datetime"]) + ", Ciudad: " + str(resultado[7]["city"]) + ", Pais: " + str(resultado[7]["country"]) + ", duracion en segundos: " + str(resultado[7]["duration (seconds)"]) + ", Forma del objeto: " + str(resultado[7]["shape"]))
        print("Fecha: " + str(resultado[6]["datetime"]) + ", Ciudad: " + str(resultado[6]["city"]) + ", Pais: " + str(resultado[6]["country"]) + ", duracion en segundos: " + str(resultado[6]["duration (seconds)"]) + ", Forma del objeto: " + str(resultado[6]["shape"]))
        print("Fecha: " + str(resultado[5]["datetime"]) + ", Ciudad: " + str(resultado[5]["city"]) + ", Pais: " + str(resultado[5]["country"]) + ", duracion en segundos: " + str(resultado[5]["duration (seconds)"]) + ", Forma del objeto: " + str(resultado[5]["shape"]))
        print("Fecha: " + str(resultado[4]["datetime"]) + ", Ciudad: " + str(resultado[4]["city"]) + ", Pais: " + str(resultado[4]["country"]) + ", duracion en segundos: " + str(resultado[4]["duration (seconds)"]) + ", Forma del objeto: " + str(resultado[4]["shape"]))
        print("Fecha: " + str(resultado[3]["datetime"]) + ", Ciudad: " + str(resultado[3]["city"]) + ", Pais: " + str(resultado[3]["country"]) + ", duracion en segundos: " + str(resultado[3]["duration (seconds)"]) + ", Forma del objeto: " + str(resultado[3]["shape"]))
            
    elif int(inputs[0]) == 4:
        time_1 = input("Ingrese las horas de entre las que desea saber los avistamientos:\n")
        time_2 = input()
        time = controller.treeTime(catalog)
        lst_info = getufosRangeTime(catalog,time_1,time_2)
        sz = lt.size(lst_info[1])
        print("El tiempo de carga fue de: " +str(time))
        print("El total de avistamnietos entre las " + time_1 +" y las "+ time_2 + " es de: " + str(lst_info[2]))
        print("---------------------------------------------------")
        print("Fecha: " +lt.getElement(lst_info[0],1)["datetime"]," Ciudad: " + lt.getElement(lst_info[0],1)["city"]," Estado: "+ lt.getElement(lst_info[0],1)["state"] ," País: " + lt.getElement(lst_info[0],1)["country"]," Duracion: " + lt.getElement(lst_info[0],1)["duration (seconds)"]," Forma: " + lt.getElement(lst_info[0],1)["shape"])
        print("---------------------------------------------------")
        print("Fecha: " +lt.getElement(lst_info[0],2)["datetime"]," Ciudad: " + lt.getElement(lst_info[0],2)["city"]," Estado: "+ lt.getElement(lst_info[0],2)["state"] ," País: " + lt.getElement(lst_info[0],2)["country"]," Duracion: " + lt.getElement(lst_info[0],2)["duration (seconds)"]," Forma: " + lt.getElement(lst_info[0],2)["shape"])
        print("---------------------------------------------------")
        print("Fecha: " +lt.getElement(lst_info[0],3)["datetime"]," Ciudad: " + lt.getElement(lst_info[0],3)["city"]," Estado: "+ lt.getElement(lst_info[0],3)["state"] ," País: " + lt.getElement(lst_info[0],3)["country"]," Duracion: " + lt.getElement(lst_info[0],3)["duration (seconds)"]," Forma: " + lt.getElement(lst_info[0],3)["shape"])
        print("---------------------------------------------------")
        print("Fecha: " +lt.getElement(lst_info[1],1)["datetime"]," Ciudad: " + lt.getElement(lst_info[1],1)["city"]," Estado: "+ lt.getElement(lst_info[1],1)["state"] ," País: " + lt.getElement(lst_info[1],1)["country"]," Duracion: " + lt.getElement(lst_info[1],1)["duration (seconds)"]," Forma: " + lt.getElement(lst_info[1],1)["shape"])
        print("---------------------------------------------------")
        print("Fecha: " +lt.getElement(lst_info[1],2)["datetime"]," Ciudad: " + lt.getElement(lst_info[1],2)["city"]," Estado: "+ lt.getElement(lst_info[1],2)["state"] ," País: " + lt.getElement(lst_info[1],2)["country"]," Duracion: " + lt.getElement(lst_info[1],2)["duration (seconds)"]," Forma: " + lt.getElement(lst_info[1],2)["shape"])
        print("---------------------------------------------------")
        print("Fecha: " +lt.getElement(lst_info[1],3)["datetime"]," Ciudad: " + lt.getElement(lst_info[1],3)["city"]," Estado: "+ lt.getElement(lst_info[1],3)["state"] ," País: " + lt.getElement(lst_info[1],3)["country"]," Duracion: " + lt.getElement(lst_info[1],3)["duration (seconds)"]," Forma: " + lt.getElement(lst_info[1],3)["shape"])
    
    
    elif int(inputs[0]) == 5:
        year_1 = input("Ingrese los años entre los que desea saber los avistamientos:\n")
        year_2 = input()
        time = controller.treeDate(catalog)
        lst_info = getufosRangeDate(catalog,year_1,year_2)
        lst_f = lst_info[1]
        lst_l = lst_info[0]
        sz = lt.size(lst_info[0])
        print("Tiempo de carga: " +str(time))
        print("El total de avistamnietos entre los años " + year_1 +" y las "+ year_2 + " es de: " + str(lst_info[2]))
        print("---------------------------------------------------")
        print("Fecha: " +lt.getElement(lst_f,1)["datetime"]," Ciudad: " + lt.getElement(lst_f,1)["city"]," Estado: "+ lt.getElement(lst_f,1)["state"] ," País: " + lt.getElement(lst_f,1)["country"]," Duracion: " + lt.getElement(lst_f,1)["duration (seconds)"]," Forma: " + lt.getElement(lst_f,1)["shape"])       
        print("---------------------------------------------------")
        print("Fecha: " +lt.getElement(lst_f,2)["datetime"]," Ciudad: " + lt.getElement(lst_f,2)["city"]," Estado: "+ lt.getElement(lst_f,2)["state"] ," País: " + lt.getElement(lst_f,2)["country"]," Duracion: " + lt.getElement(lst_f,2)["duration (seconds)"]," Forma: " + lt.getElement(lst_f,2)["shape"]) 
        print("---------------------------------------------------")
        print("Fecha: " +lt.getElement(lst_f,3)["datetime"]," Ciudad: " + lt.getElement(lst_f,3)["city"]," Estado: "+ lt.getElement(lst_f,3)["state"] ," País: " + lt.getElement(lst_f,3)["country"]," Duracion: " + lt.getElement(lst_f,3)["duration (seconds)"]," Forma: " + lt.getElement(lst_f,3)["shape"]) 
        print("---------------------------------------------------")
        print("Fecha: " +lt.getElement(lst_l,1)["datetime"]," Ciudad: " + lt.getElement(lst_l,1)["city"]," Estado: "+ lt.getElement(lst_l,1)["state"] ," País: " + lt.getElement(lst_l,1)["country"]," Duracion: " + lt.getElement(lst_l,1)["duration (seconds)"]," Forma: " + lt.getElement(lst_l,1)["shape"])
        print("---------------------------------------------------")
        print("Fecha: " +lt.getElement(lst_l,2)["datetime"]," Ciudad: " + lt.getElement(lst_l,2)["city"]," Estado: "+ lt.getElement(lst_l,2)["state"] ," País: " + lt.getElement(lst_l,2)["country"]," Duracion: " + lt.getElement(lst_l,2)["duration (seconds)"]," Forma: " + lt.getElement(lst_l,2)["shape"])
        print("---------------------------------------------------")
        print("Fecha: " +lt.getElement(lst_l,3)["datetime"]," Ciudad: " + lt.getElement(lst_l,3)["city"]," Estado: "+ lt.getElement(lst_l,3)["state"] ," País: " + lt.getElement(lst_l,3)["country"]," Duracion: " + lt.getElement(lst_l,3)["duration (seconds)"]," Forma: " + lt.getElement(lst_l,3)["shape"])

    elif int(inputs[0]) == 6:
        lomin = float(input("Ingrese el rango de lngitud:\n"))
        lomax = float(input())
        lamin = float(input("Ingrese el rango de latitud:\n"))
        lamax = float(input())
        time = controller.treeLongitud(catalog,lomin,lomax,lamin,lamax)
        lst_c = controller.zone(catalog)
        print("El tiempo de carga fue de: "+str(time))
        print(lst_c)



    else:
        sys.exit(0)
sys.exit(0)
