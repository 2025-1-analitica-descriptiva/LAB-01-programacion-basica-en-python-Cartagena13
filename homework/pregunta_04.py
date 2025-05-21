"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

from collections import Counter
from collections import defaultdict
import csv
import os
def pregunta_04():
    base_dir = os.path.dirname(__file__)
    ruta_csv = os.path.join(base_dir, "..", "files", "input", "data.csv")
    conteo=defaultdict(int)


    with open(ruta_csv) as file:
        archivo = csv.reader(file, delimiter="\t")
        for line in archivo:
            fecha=line[2]
            mes=fecha.split("-")[1]
            valor=line[1]
            conteo[mes]+=int((int(valor)/int(valor)) if int(valor) != 0 else 1)
    return(sorted(conteo.items()))
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
