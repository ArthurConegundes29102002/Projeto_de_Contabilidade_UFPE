import pandas as pd
import pathlib
#this_path= pathlib.Path()
this_file_path = pathlib.Path('HeC.csv')
table_reading = pd.read_csv(this_file_path)
real_table = table_reading
#-------------------------------------------
def print_table():
    print(real_table)
#print_table()        
#------------------------------------------- buscando apenas os dados do RS
estado = input('digite o estado que você deseja >>')
find_state= table_reading['UF'] == estado
print(table_reading.loc[find_state])