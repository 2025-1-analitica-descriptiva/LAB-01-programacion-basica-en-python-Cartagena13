"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv
import os
def pregunta_01():
    base_dir = os.path.dirname(__file__)
    ruta_csv = os.path.join(base_dir, "..", "files", "input", "data.csv")

    suma=0
    with open(ruta_csv) as file:
        lector = csv.reader(file, delimiter="\t")
        for fila in lector:
            #print(fila[1])
            suma += int(fila[1])
        return suma

"""
    Retorne la suma de la segunda columna.

    Rta/
    214
    
    """
