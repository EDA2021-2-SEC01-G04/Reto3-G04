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
 """

import config as cf
import model
import csv
import time as t

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def init():
    """
    Llama la funcion de inicializacion  del modelo.
    """
    # catalog es utilizado para interactuar con el modelo
    analyzer = model.newAnalyzer()
    return analyzer
# Funciones para la carga de datos
def loadArtists(analyzer):
    star_time = t.process_time()
    artistfile = cf.data_dir + "UFOS/UFOS-utf8-small.csv"
    input_file = csv.DictReader(open(artistfile,encoding="utf-8"))

    for artist in input_file:
        model.addsightings(analyzer, artist)
    end_time = t.process_time()
    laps_time = (end_time - star_time)*1000
    return (laps_time)

def treeTime(analiyzer):
    return model.treeTime(analiyzer)
def treeDate(analiyzer):
    return model.treeDate(analiyzer)
def treeLongitud(analyzer):
    return model.treeLongitud(analyzer)

# Funciones para la carga de datos

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
def getUfosByCity(analyzer,city):
    return model.getUfosByCity(analyzer,city)
def cityHeight(analyzer):
    """
    Altura del arbol
    """
    return model.cityHeight(analyzer)
def getufosRangeTime(analyzer,time1,time2):
    return model.getufosRangeTime(analyzer,time1,time2)

def getufosRangeDate(analyzer,time1,time2):
    return model.getufosRangeDate(analyzer,time1,time2)

def getufoscoLatitud(analyzer,long1,long2,lat1,lat2):
    return model.getufoscoLatitud(analyzer,long1,long2,lat1,lat2)

def mayorHora(analyzer):

    return model.mayorHora(analyzer)