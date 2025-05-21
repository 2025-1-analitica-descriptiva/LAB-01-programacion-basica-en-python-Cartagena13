"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


import os
import csv
from collections import defaultdict

def pregunta_12():
    suma_por_letra = defaultdict(int)

    base_dir = os.path.dirname(__file__)
    ruta_csv = os.path.join(base_dir, "..", "files", "input", "data.csv")
    with open(ruta_csv) as file:
        archivo = csv.reader(file, delimiter="\t")

        for line in archivo:
            par=line[4].split(",")
            letra1=line[0]
            for i in par:
                valor=int(i.split(":")[1])
                suma_por_letra[letra1] += valor
    suma_dict = dict(sorted(suma_por_letra.items()))

    return suma_dict   
    
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
