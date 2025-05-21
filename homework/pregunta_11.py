"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


import os
import csv
from collections import defaultdict

def pregunta_11():
    suma_por_letra = defaultdict(int)

    base_dir = os.path.dirname(__file__)
    ruta_csv = os.path.join(base_dir, "..", "files", "input", "data.csv")
    with open(ruta_csv) as file:
        archivo = csv.reader(file, delimiter="\t")

        for line in archivo:
            valor=int(line[1])
            letras=line[3].split(",")
            for letra in letras:
                suma_por_letra[letra] += valor
    suma_dict = dict(sorted(suma_por_letra.items()))

    return suma_dict
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
