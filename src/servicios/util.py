import csv
import pandas as pd

from src.config import configuration


def convertir_csv_widgets(file_path, file_path_out, filtros_tag):
    if not filtros_tag:
        print('Reformateando CSV >> No hay tags filtro.')
    else:
        print('Reformateando CSV >> Tags filtro:')
        for i in filtros_tag:
            print('Reformateando CSV >> - ' + i)

    df = pd.read_csv(file_path, encoding='utf-8')
    widgets = list(df.widgets.unique())  # provide list unique of entities
    arr_csv = pd.read_csv(file_path, header=None)

    # Compara los widgets unicos contra el array del CSV
    arr = []
    for w in widgets:
        w_tags = ''
        exist_tag = False
        for wid, tag, val in arr_csv.values:
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
