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
    print("3- ")
    print("4- Contar avistamientos por Hora/Minutos del día")
    print("5- Contar los avistamientos en un rango de fechas")
    print("6- ")
catalog = None

def getufosRangeTime(analyzer,time1,time2):
    return controller.getufosRangeTime(analyzer,time1,time2)


def getufosRangeDate(analyzer,time1,time2):
    return controller.getufosRangeDate(analyzer,time1,time2)

def top3(lst):
    i = 0

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = controller.init()
        controller.loadArtists(catalog)
        print('Altura del arbol: ' + str(controller.cityHeight(catalog)))
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
            
    elif int(inputs[0]) == 4:
        time_1 = input("Ingrese las horas de entre las que desea saber los avistamientos:\n")
        time_2 = input()
        controller.treeTime(catalog)
        lst_info = getufosRangeTime(catalog,time_1,time_2)
        sz = lt.size(lst_info[1])
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
        controller.treeDate(catalog)
        lst_info = getufosRangeDate(catalog,year_1,year_2)
        lst_f = lst_info[1]
        lst_l = lst_info[0]
        sz = lt.size(lst_info[0])
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
        pass


    else:
        sys.exit(0)
sys.exit(0)
