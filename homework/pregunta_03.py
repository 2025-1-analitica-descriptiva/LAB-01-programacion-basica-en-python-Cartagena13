"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv
import os
from collections import defaultdict
def pregunta_03():

    base_dir = os.path.dirname(__file__)
    ruta_csv = os.path.join(base_dir, "..", "files", "input", "data.csv")
    sumletra=defaultdict(int)
    with open(ruta_csv) as file:
        archivo = csv.reader(file, delimiter="\t")
        for line in archivo:
            letra=line[0]
            valor=line[1]
            sumletra[letra]+=int(valor)
    return(sorted(sumletra.items()))
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
