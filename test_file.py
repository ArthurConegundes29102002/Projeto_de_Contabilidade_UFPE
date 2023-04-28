import pandas as pd
import pathlib


#this_path= pathlib.Path()
this_file_path = pathlib.Path('Planilha de teste.xlsx')

table_reading = pd.read_excel('Planilha de teste.xlsx')

#retorna todos os nomes sem repetições
def function1(table):
    all_names=[]
    name_column = table['Nome']

    for x in name_column:
        if x not in all_names:
            all_names.append(x)
        else:
            pass
    return print(all_names)

# todos_os_nomes = []
# name_column = table_reading['Nome']

# for x in name_column:
#     if x not in name_column:
#         name_column.append(x)

function1(table_reading)