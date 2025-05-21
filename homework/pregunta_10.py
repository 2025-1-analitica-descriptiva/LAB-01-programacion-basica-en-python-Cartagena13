"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


import os
import csv
def pregunta_10():
    resultado = []

    base_dir = os.path.dirname(__file__)
    ruta_csv = os.path.join(base_dir, "..", "files", "input", "data.csv")
    with open(ruta_csv) as file:
        archivo = csv.reader(file, delimiter="\t")

        for line in archivo:
            letra=line[0]
            col4=line[3]
            col5=line[4]
            cant_col4=len(col4.split(","))
            cant_col5=len(col5.split(","))
            resultado.append((letra, cant_col4, cant_col5))
    return resultado

    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
