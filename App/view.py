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
        controller.loadArtists(catalog)
        print('Altura del arbol: ' + str(controller.cityHeight(catalog)))
        print("El totalde avistamients cargados fue de: " + str(lt.size(catalog["ufos"])))

    elif int(inputs[0]) == 2:
        city = input("Ingrese el nombre de la ciudad\n")
        controller.loadArtists(catalog)
        lst = controller.getUfosByCity(catalog,city)
        size = lt.size(lst)
        if lst is str:
            print(lst)
        else:
            print("El total de avistamiento en " + city + "fue de: " + str(size))
            print(lt.getElement(lst,1))
            print(lt.getElement(lst,1))
            print(lt.getElement(lst,1))

            
    elif int(inputs[0]) == 4:
        time_1 = input("Ingrese las horas de entre las que desea saber los avistamientos:\n")
        time_2 = input()
        controller.treeTime(catalog)
        lst_info = getufosRangeTime(catalog,time_1,time_2)
        sz = lt.size(lst_info[1])
        print("El total de avistamnietos entre las " + time_1 +" y las "+ time_2 + " es de: " + str(lst_info[2]))
        print(lt.getElement(lst_info[0],1))
        print("---------------------------------------------------")
        print(lt.getElement(lst_info[0],2))
        print("---------------------------------------------------")
        print(lt.getElement(lst_info[0],3))
        print("---------------------------------------------------")
        print(lt.getElement(lst_info[1],sz))
        print("---------------------------------------------------")
        print(lt.getElement(lst_info[1],sz-1))
        print("---------------------------------------------------")
        print(lt.getElement(lst_info[1],sz-2))
    
    
    elif int(inputs[0]) == 5:
        year_1 = input("Ingrese los años entre los que desea saber los avistamientos:\n")
        year_2 = input()
        controller.treeDate(catalog)
        lst_info = getufosRangeDate(catalog,year_1,year_2)
        sz = lt.size(lst_info[0])
        print("El total de avistamnietos entre los años " + year_1 +" y las "+ year_2 + " es de: " + str(lst_info[1]))
        print(lt.getElement(lst_info[0],1))
        print("---------------------------------------------------")
        print(lt.getElement(lst_info[0],2))
        print("---------------------------------------------------")
        print(lt.getElement(lst_info[0],3))
        print("---------------------------------------------------")
        print(lt.getElement(lst_info[0],sz))
        print("---------------------------------------------------")
        print(lt.getElement(lst_info[0],sz-1))
        print("---------------------------------------------------")
        print(lt.getElement(lst_info[0],sz-2))

    else:
        sys.exit(0)
sys.exit(0)
