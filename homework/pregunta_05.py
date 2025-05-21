"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import os
import csv
def pregunta_05():
    base_dir = os.path.dirname(__file__)
    ruta_csv = os.path.join(base_dir, "..", "files", "input", "data.csv")
    resul=[]
    group={}
    with open(ruta_csv) as file:
        archivo = csv.reader(file, delimiter="\t")
        for line in archivo:
            letra=line[0]
            valor=int(line[1])
            if letra in group:
                group[letra].append(valor)
            else:
                group[letra]=[valor]
    for letra in sorted(group.keys()):
        maxi=max(group[letra])
        mini=min(group[letra])
        resul.append((letra, maxi, mini))
    return(resul) 


    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
