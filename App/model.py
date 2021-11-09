﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """



import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
import datetime
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newAnalyzer():
    """ Inicializa el analizador

    Crea una lista vacia para guardar todos los crimenes
    Se crean indices (Maps) por los siguientes criterios:
    -Fechas

    Retorna el analizador inicializado.
    """
    analyzer = {'crimes': None,
                'dateIndex': None
                }

    analyzer['ufos'] = lt.newList('SINGLE_LINKED')
    analyzer['city'] = om.newMap(omaptype='BST')
    analyzer["hour"] = om.newMap(omaptype='BST')
    analyzer["date"] = om.newMap(omaptype='BST')
    return analyzer
# Funciones para agregar informacion al catalogo

# ---------------Punto 1-----------------------------
def addsightings(analyzer, ufo):
    """
    """
    lt.addLast(analyzer['ufos'], ufo)
    updateDatetime(analyzer['city'], ufo)
    return analyzer

def updateDatetime(mapa,ufo):
    actualct = ufo["city"]
    
    entry = om.get(mapa, actualct)
    if entry == None :
         timentry = newDataEntry(actualct)
         lt.addLast(timentry["lstufos"],ufo)
         om.put(mapa, actualct,timentry)
    else:
        timentry = me.getValue(entry)
        lt.addLast(timentry["lstufos"],ufo)
    return mapa 

def newDataEntry(ct):
    """
    Crea una entrada en el indice por fechas, es decir en el arbol
    binario.
    """
    entry = {'city': None, 'lstufos': None}
    entry['city'] = ct
    entry['lstufos'] = lt.newList('SINGLE_LINKED',)
    return entry

def newCityEntry(city, crime):
    """
    Crea una entrada en el indice por tipo de crimen, es decir en
    la tabla de hash, que se encuentra en cada nodo del arbol.
    """
    ctentry = {'city': None, 'lstctufos': None}
    ctentry['city'] = city
    ctentry['lstctufos'] = lt.newList('SINGLELINKED')
    return ctentry


# ------------Punto 3------------
def treeTime(analiyzer):
    lst_ufo = analiyzer["ufos"]
    for ufo in lt.iterator(lst_ufo):
        time = datetime.datetime.strptime(ufo["datetime"],'%Y-%m-%d %H:%M:%S')
        time = str(time.time())
        entry = om.get(analiyzer["hour"],time)
        if entry == None:
            timentry = newTime()
            lt.addLast(timentry,ufo)
            om.put(analiyzer["hour"],time,timentry)
        else:
            timentry = me.getValue(entry)
            lt.addLast(timentry,ufo)

def newTime():
    tmentry = lt.newList('SINGLELINKED')
    return tmentry
#--------------------Punt 4-------------
def treeDate(analiyzer):
    lst_ufo = analiyzer["ufos"]
    for ufo in lt.iterator(lst_ufo):
        time = datetime.datetime.strptime(ufo["datetime"],'%Y-%m-%d %H:%M:%S')
        time = str(time.date())
        entry = om.get(analiyzer["date"],time)
        if entry == None:
            timentry = newDate()
            lt.addLast(timentry,ufo)
            om.put(analiyzer["date"],time,timentry)
        else:
            timentry = me.getValue(entry)
            lt.addLast(timentry,ufo)

def newDate():
    tmentry = lt.newList('SINGLELINKED')
    return tmentry
# Funciones para creacion de datos

# Funciones de consulta
#-------Punto 1-----------------------
def getUfosByCity(analyzer,city):
    lst = om.get(analyzer["city"],city)
    lst = me.getValue(lst)["lstufos"]
    if lst != None:
        lst_srt = sa.sort(lst,compareDates)
        return lst_srt 
    else:
        return "no hay avistamientos en esta ciudad"

    
def cityHeight(analyzer):
    """
    Altura del arbol
    """
    return om.height(analyzer['city'])

#------------Punto 3----------------------------
def getufosRangeTime(analyzer,time1,time2):
    time1 = time1+"00"
    time2 = time2+"00"
    lst_ufos = om.values(analyzer["hour"],time1,time2)
    sz = lt.size(lst_ufos)
    lst_les = lt.getElement(lst_ufos,1)
    lst_hig = lt.getElement(lst_ufos,sz)
    lst_hig = sa.sort(lst_hig,compareDate1)
    lst_les = sa.sort(lst_les,compareDate2)
    total = getTotalLst(lst_ufos)
    return (lst_les,lst_hig,total)

def getTotalLst(lst):
    total = 0
    for hora in lt.iterator(lst):
        total += lt.size(hora)
    return total
def mayorHora(analyzer):
    return om.maxKey(analyzer["hour"])
#-------------------Punt 4------------------
def getufosRangeDate(analyzer,time1,time2):
    lst_ufos = om.values(analyzer["date"],time1,time2)
    total = getTotalLst(lst_ufos)
    return (lst_ufos,total)


# Funciones utilizadas para comparar elementos dentro de una lista
def compareDates(date1, date2):
    fecha_1 = datetime.datetime.strptime(date1["datetime"], '%Y-%m-%d %H:%M:%S')
    fecha_2 = datetime.datetime.strptime(date2["datetime"], '%Y-%m-%d %H:%M:%S')
    if (fecha_1 < fecha_2):
        return 0
    elif (fecha_1 > fecha_2):
        return 1
def compareDate1(date1, date2):
    fecha_1 = datetime.datetime.strptime(date1["datetime"], '%Y-%m-%d %H:%M:%S')
    fecha_2 = datetime.datetime.strptime(date2["datetime"], '%Y-%m-%d %H:%M:%S')
    if (fecha_1.date() > fecha_2.date()):
        return 0
    else:
        return 1
def compareDate2(date1, date2):
    fecha_1 = datetime.datetime.strptime(date1["datetime"], '%Y-%m-%d %H:%M:%S')
    fecha_2 = datetime.datetime.strptime(date2["datetime"], '%Y-%m-%d %H:%M:%S')
    if (fecha_1.date() > fecha_2.date()):
        return 1
    else:
        return 0
def compareTime1(date1, date2):
    fecha_1 = datetime.datetime.strptime(date1["datetime"], '%Y-%m-%d %H:%M:%S')
    fecha_2 = datetime.datetime.strptime(date2["datetime"], '%Y-%m-%d %H:%M:%S')
    if (fecha_1.time() > fecha_2.time()):
        return 1
    else:
        return 0
# Funciones de ordenamiento
