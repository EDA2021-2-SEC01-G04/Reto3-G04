"""
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
import time as t
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
    analyzer["longitud"] = om.newMap(omaptype='BST')
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
# ------------Punto 2------------
def sightingsByDuration(analyzer,min,max):
    duracion_max = 0
    contador = 0
    lista = lt.newList("SINGLE_LINKED")
    for ufo in lt.iterator(analyzer['ufos']):
        duration = float(ufo['duration (seconds)'])
        if duration > duracion_max:
            duracion_max = duration
    
    for ufo in lt.iterator(analyzer['ufos']):
        if float(ufo['duration (seconds)']) == duracion_max:
            contador += 1
        if float(ufo['duration (seconds)']) >= min and float(ufo['duration (seconds)']) <= max:
            lt.addLast(lista,ufo)

    sa.sort(lista,compareDuration)
    size = lt.size(lista)
    retorno = [duracion_max,contador,size,lt.getElement(lista,1),lt.getElement(lista,2),lt.getElement(lista,3),lt.getElement(lista,size-2),lt.getElement(lista,size-1),lt.getElement(lista,size)]


    return retorno

# ------------Punto 3------------
def treeTime(analiyzer):
    star_time = t.process_time()
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
    end_time = t.process_time()
    laps_time = (end_time - star_time)*1000      
    return laps_time
def newTime():
    tmentry = lt.newList('SINGLELINKED')
    return tmentry
#--------------------Punt 4-------------
def treeDate(analiyzer):
    star_time = t.process_time()
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
    end_time = t.process_time()
    laps_time = (end_time - star_time)*1000      
    return laps_time

def newDate():
    tmentry = lt.newList('SINGLELINKED')
    return tmentry

#------Punto 5--------------------------------
def treeLongitud(analyzer):
    star_time = t.process_time()
    lst_ufos = analyzer["ufos"]
    for ufo in lt.iterator(lst_ufos):
        long = str(round(float(ufo["longitude"]),2))
        entry = om.get(analyzer["longitud"],long)
        if entry == None:
            long_entry = newLong()
            addLongitu(long_entry,ufo)
            om.put(analyzer["longitud"],long,long_entry)
        else:
            long_entry = me.getValue(entry)
            addLongitu(long_entry,ufo)
    
    
    end_time = t.process_time()
    laps_time = (end_time - star_time)*1000      
    return laps_time
def addLongitu(data_entry,ufo):
    long_entry = mp.get(data_entry,str(round(float(ufo["latitude"]),2)))
    if long_entry == None:
        entry = newLatitud(str(round(float(ufo["latitude"]),2)))
        lt.addLast(entry["lstlatitud"],ufo)
        mp.put(data_entry,str(round(float(ufo["latitude"]),2)),entry)
    else:
        entry = me.getValue(long_entry)
        lt.addLast(entry["lstlatitud"],ufo)

def newLong():
    entry = mp.newMap(numelements=200,maptype='PROBING')
    return entry
def newLatitud(latitud):
    entry = {'latitud': None, 'lstlatitud': None}
    entry['latitud'] = latitud
    entry['lstlatitud'] = lt.newList('SINGLELINKED')
    return entry





# Funciones para creacion de datos

# Funciones de consulta
#-------Punto 1-----------------------
def getUfosByCity(analyzer,city):
    lst = om.get(analyzer["city"],city)
    lst = me.getValue(lst)["lstufos"]
    if lst != None:
        lst_srt = sa.sort(lst,compareDate2)
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
    time1 = time1+":00"
    time2 = time2+":00"
    lst_ufos = om.values(analyzer["hour"],time1,time2)
    lst_les = lt.getElement(lst_ufos,1)
    lst_hig = om.get(analyzer["hour"],time2)
    lst_hig = me.getValue(lst_hig)
    lst_hig = sa.sort(lst_hig,compareDate2)
    lst_les = sa.sort(lst_les,compareDate1)
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
    lst_first = iterateLst(lst_ufos)
    lst_last = iteratelstLast(lst_ufos)
    total = getTotalLst(lst_ufos)
    return (lst_last,lst_first,total)

def iterateLst(lst):
    i = lt.newList()
    for j in lt.iterator(lst):
        if lt.size(j) >= 3 and lt.size(i) < 3:
            element1 = lt.getElement(j,1)
            element2 = lt.getElement(j,2)
            element3 = lt.getElement(j,3)
            lt.addLast(i,element1)
            lt.addLast(i,element2)
            lt.addLast(i,element3)
            break
        if lt.size(j) == 2 and lt.size(i) < 3:
            element1 = lt.getElement(j,1)
            element2 = lt.getElement(j,2)
            lt.addLast(i,element1)
            lt.addLast(i,element2)
        if lt.size(j) == 1 and lt.size(i) < 3:
            element1 = lt.getElement(j,1)
            lt.addLast(i,element1)

        if lt.size(i) >= 3:
            return i
def iteratelstLast(lst):
    sz = lt.size(lst)
    i = lt.newList()
    element = lt.getElement(lst,sz)
    if lt.size(element) >= 3:
        element1 = lt.getElement(element,1)
        element2 = lt.getElement(element,2)
        element3 = lt.getElement(element,3)
        lt.addLast(i,element1)
        lt.addLast(i,element2)
        lt.addLast(i,element3)
    if lt.size(element) == 2:
        element1 = lt.getElement(element,1)
        element2 = lt.getElement(element,2)
        element3 = lt.getElement(lst,sz-1)
        element3 = lt.getElement(element3,1)
        lt.addLast(i,element1)
        lt.addLast(i,element2)
        lt.addLast(i,element3)
    if lt.size(element) == 1 and lt.size(lt.getElement(lst,sz-1)) > 1 :
        element1 = lt.getElement(element,1)
        element2 = lt.getElement(lst,sz-1)
        element2 = lt.getElement(element2,1)
        element3 = lt.getElement(lst,sz-1)
        element3 = lt.getElement(element3,2)
        lt.addLast(i,element1)
        lt.addLast(i,element2)
        lt.addLast(i,element3)

    if lt.size(element) == 1 and lt.size(lt.getElement(lst,sz-1)) == 1:
        element1 = lt.getElement(element,1)
        element2 = lt.getElement(lst,sz-1)
        element2 = lt.getElement(element2,1)
        element3 = lt.getElement(lst,sz-2)
        element3 = lt.getElement(element3,1)
        lt.addLast(i,element1)
        lt.addLast(i,element2)
        lt.addLast(i,element3)

    return i 
#----------------Punto 5---------------------
def getufoscoLatitud(analyzer,long1,long2,lat1,lat2):
    lst = om.values(analyzer["longitud"],long1,long2)
    lst = iterateLstValues(lst,lat1,lat2)
    print(lst)
    return lst

def iterateLstValues(lst,lat1,lat2):
    lista = lt.newList()
    for l in lt.iterator(lst):
        if mp.contains(l,lat1):
            k = mp.get(l,lat1)
            k = me.getValue(k)["lstlatitud"]
            lt.addLast(lista,k)
        if mp.contains(l,lat2):
            k = mp.get(l,lat2)
            k = me.getValue(k)["lstlatitud"]
            lt.addLast(lista,k)

    return lista
# Funciones utilizadas para comparar elementos dentro de una lista
def compareDates(date1, date2):
    fecha_1 = datetime.datetime.strptime(date1["datetime"], '%Y-%m-%d %H:%M:%S')
    fecha_2 = datetime.datetime.strptime(date2["datetime"], '%Y-%m-%d %H:%M:%S')
    if (fecha_1 < fecha_2):
        return 1
    elif (fecha_1 > fecha_2):
        return 0

def compareDuration(d1,d2):
    if (float(d1['duration (seconds)']) < float(d2['duration (seconds)'])):
        return 0
    elif (float(d1['duration (seconds)']) > float(d2['duration (seconds)'])):
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
