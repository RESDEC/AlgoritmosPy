from __future__ import print_function
import pandas as pd
import numpy as np


def convertir_csv_widgets(file_path, file_path_out, filtros_tag, sep):
    if not filtros_tag:
        print('Reformateando CSV >> No hay tags filtro.')
    else:
        print('Reformateando CSV >> Tags filtro:')
        for i in filtros_tag:
            print('Reformateando CSV >> - ' + i)

    df = pd.read_csv(file_path, encoding='utf-8', sep=sep)
    widgets = list(df.widgets.unique())  # provide list unique of entities
    arr_csv = pd.read_csv(file_path, header=None, sep=sep)

    # Compara los widgets unicos contra el array del CSV
    arr = []
    for w in widgets:
        w_tags = ''
        exist_tag = False
        # for wid, tag, val in arr_csv.values:
        for wid, tag in arr_csv.values:
            if wid == w:
                w_tags += tag + ' '
                for f in filtros_tag:
                    if f in tag:
                        exist_tag = True
                        break
        if not filtros_tag:
            arr.append([w_tags, w])
        else:
            if exist_tag:
                arr.append([w_tags, w])

    arr_out = pd.DataFrame(arr)
    arr_out.to_csv(file_path_out, index=False, header=['tags', 'widgets'])


def corregir_csv(file_path, file_path_out, sep):
    print('Corrigiendo CSV >> Leyendo archivo ' + file_path)
    arr_csv = []
    i = 0
    for line in open(file_path):
        arr = line.split(sep)
        i += 1
        if arr.__len__() == 3:
            arr_new = [arr[0], arr[1], arr[2].replace("\n", "")]
        else:
            print('Corrigiendo CSV >> Se ha encontrado una fila con errores, corrigiendo. Fila: ' + str(i))
            x = 1
            y = arr.__len__() - 1
            tag = ''
            while x < y:
                tag += arr[x]
                x += 1

            arr_new = [arr[0], tag, arr[y].replace("\n", "")]

        arr_csv.append(arr_new)
    arr_out = pd.DataFrame(arr_csv)
    arr_out.to_csv(file_path_out, index=False, header=False, sep=sep)
    print('Corrigiendo CSV >> Se ha generado el archivo: ' + file_path_out)
