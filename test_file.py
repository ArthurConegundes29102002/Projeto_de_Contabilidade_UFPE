import pandas as pd
import pathlib

#this_path= pathlib.Path()
this_file_path = pathlib.Path('Planilha de teste.xlsx')

table_reading = pd.read_excel('Planilha de teste.xlsx')

#print(table_reading[['Nome','Idade','Altura']])
table_reading['Estado'] == 'SP'
print(table_reading.loc[table_reading['Estado'] == 'SP'])