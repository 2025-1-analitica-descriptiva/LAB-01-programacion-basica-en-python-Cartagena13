"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


import os
import csv
from collections import defaultdict
def pregunta_09():
    dicc=defaultdict(int)

    base_dir = os.path.dirname(__file__)
    ruta_csv = os.path.join(base_dir, "..", "files", "input", "data.csv")
    with open(ruta_csv) as file:
        archivo = csv.reader(file, delimiter="\t")

        for line in archivo:
            col=line[4]
            pares=col.split(",")

            for i in pares:
                clave,_=i.split(":")
                dicc[clave]+=1
    conteo_dict = dict(sorted(dicc.items()))
    return conteo_dict

    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
