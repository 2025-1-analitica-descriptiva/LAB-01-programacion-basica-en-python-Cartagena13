"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv
import os
from collections import Counter

def pregunta_02():
    #busca la data
    base_dir = os.path.dirname(__file__)
    ruta_csv = os.path.join(base_dir, "..", "files", "input", "data.csv")
    # recorre el archivo y almacena la data: cada fila es una lista compuesta de los elementos de cada columna
    with open(ruta_csv) as file:
        archivo = csv.reader(file, delimiter="\t")
        letra= [fila[0] for fila in archivo]
        count=Counter(letra)
    return sorted(count.items())







"""
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
