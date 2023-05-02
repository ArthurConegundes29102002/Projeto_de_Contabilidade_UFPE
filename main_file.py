import pandas as pd
import pathlib
from IPython.display import display
#locale vai servir pra transformar numeros com vírgulas
import locale
locale.setlocale(locale.LC_NUMERIC, 'en_DK.UTF-8')
this_file_path = pathlib.Path('HeC.csv')
Table = pd.read_csv(this_file_path)

#------------------------------------------- Printa toda a Tabela:

def print_table(table):
    display(table)

#------------------------------------------- Retorna Todos os Municípios do Estado desejado:

def municipios_finder_2(table,state):
    municipios = []
    this_table = table[['Instituição','UF']]

    for x in this_table['Instituição']:
        deusmeajuda = x.replace(' ','').split('-')
        if deusmeajuda[-1] == state:
            if x not in municipios:
                municipios.append(x)
        else:
            pass

    return (municipios)

#------------------------------------------- exibindo todas as linhas referentes a determinada Prefeitura:

def municipios_statistics(prefeitura,table):
    prefecture_table = table.loc[table['Instituição']==prefeitura]
    return prefecture_table

#------------------------------------------- exibindo todas as estatísticas de determinada prefeitura:
def municipios_specific_statistics(table,Column_Name,Column_information):
    #List = [(),(),(),(),()]
    List = [0,0,0,0,0]
    #esquema = [segurança,assistencia social, previdencia social, saúde,educação]

    paia = table.loc[table[Column_Name]== Column_information,['Instituição','Coluna','Conta','Valor']]
    
    # lendo o valor das tabelas de cada um dos tópicos pedidos :

    educacao = paia.loc[paia['Conta']== '12 - Educação',['Valor']]
                        
    saude = paia.loc[paia['Conta']== '10 - Saúde',['Valor']]
                     
    previdencia = paia.loc[paia['Conta']== '09 - Previdência Social',['Valor']]
                           
    seguranca_publica = paia.loc[paia['Conta']== '06 - Segurança Pública',['Valor']]

    assistencia_social = paia.loc[paia['Conta']== '08 - Assistência Social',['Valor']]

    for x in seguranca_publica['Valor']:
        number = locale.atof(x)
        List[0]=number

    for x in assistencia_social['Valor']:
        number = locale.atof(x)
        List[1]=number

    for x in previdencia['Valor']:
        number = locale.atof(x)
        List[2]=number

    for x in saude['Valor']:
        number = locale.atof(x)
        List[3]=number

    for x in educacao['Valor']:
        number = locale.atof(x)
        List[4]=number
    return(List)

#------------------------------------------- Função Principal(por estado)

def State_Statistics(table,state):
    #a sum list vai servir para que no final possamos somar todos os valores dos municípios dos estados
    sum_list = [0,0,0,0,0]
    Lista_Municipios_Gerais = municipios_finder_2(table,state)

    DE_geral = 0
    DL_geral = 0
    DP_geral = 0
    IRPNP_geral = 0
    IRPP_geral = 0

    for x in Lista_Municipios_Gerais:

        Lista_DO_municipio = municipios_statistics(x,table)

        DE = municipios_specific_statistics(Lista_DO_municipio,'Coluna','Despesas Empenhadas')

        DL = municipios_specific_statistics(Lista_DO_municipio,'Coluna','Despesas Liquidadas')
    
        DP = municipios_specific_statistics(Lista_DO_municipio,'Coluna','Despesas Pagas')

        IRPNP = municipios_specific_statistics(Lista_DO_municipio,'Coluna','Inscrição de Restos a Pagar Não Processados')

        IRPP = municipios_specific_statistics(Lista_DO_municipio,'Coluna','Inscrição de Restos a Pagar Processados')
        
        DE_geral = DE_geral + DE[0] + DE[1] + DE[2] + DE[3] + DE[4]
        DL_geral = DL_geral + DL[0] + DL[1] + DL[2] + DL[3] + DL[4]
        DP_geral = DP_geral + DP[0] + DP[1] + DP[2] + DP[3] + DP[4]
        IRPNP_geral = IRPNP_geral + IRPNP[0] + IRPNP[1] + IRPNP[2] + IRPNP[3] + IRPNP[4]
        IRPP_geral = IRPP_geral + IRPP[0] + IRPP[1] + IRPP[2] + IRPP[3] + IRPP[4]

    print(f'Despesas Empenhadas do estado de {state} --> {DE_geral}')

    print(f'Despesas Liquidadas do estado de {state} --> {DL_geral}')

    print(f'Despesas Pagas do estado de {state} --> {DP_geral}')

    print(f'Inscrições de Restos a Pagar Não Processados do estado de {state} --> {IRPNP_geral}')
    
    print(f'Inscrições de Restos a Pagar Processados do estado de {state} --> {IRPP_geral}')

#------------------------------------------- Função Principal(por Município)

def Municipio_Statistics(table,state):

    Lista_Municipios_Gerais = municipios_finder_2(table,state)
    fim = False

    try:
        while fim == False:
            county = input('Digite o nome do Município >>')
            if county not in Lista_Municipios_Gerais:
                print(f'Infelizmente esse município não pertence a esse estado')
            
            else:
            
                Lista_DO_municipio = municipios_statistics(county,table)

                DE = municipios_specific_statistics(Lista_DO_municipio,'Coluna','Despesas Empenhadas')

                DL = municipios_specific_statistics(Lista_DO_municipio,'Coluna','Despesas Liquidadas')
            
                DP = municipios_specific_statistics(Lista_DO_municipio,'Coluna','Despesas Pagas')

                IRPNP = municipios_specific_statistics(Lista_DO_municipio,'Coluna','Inscrição de Restos a Pagar Não Processados')

                IRPP = municipios_specific_statistics(Lista_DO_municipio,'Coluna','Inscrição de Restos a Pagar Processados')

                print(f'{county}\nDespesas Empenhadas :')

                print(f'segurança = {DE[0]}\nassistencia social = {DE[1]}\nprevidencia social = {DE[2]}\nsaúde = {DE[3]}\neducação = {DE[4]} ')
                #-------------------------------------------
                print(f'\nDespesas Liquidadas :')

                print(f'segurança = {DL[0]}\nassistencia social = {DL[1]}\nprevidencia social = {DL[2]}\nsaúde = {DL[3]}\neducação = {DL[4]} ')
                #-------------------------------------------
                print(f'\nDespesas Pagas :')

                print(f'segurança = {DP[0]}\nassistencia social = {DP[1]}\nprevidencia social = {DP[2]}\nsaúde = {DP[3]}\neducação = {DP[4]} ')
                #-------------------------------------------
                print(f'\nDespesas Inscrição de Restos a Pagar Não Processados :')

                print(f'segurança = {IRPNP[0]}\nassistencia social = {IRPNP[1]}\nprevidencia social = {IRPNP[2]}\nsaúde = {IRPNP[3]}\neducação = {IRPNP[4]} ')
                #-------------------------------------------
                print(f'\nDespesas Inscrição de Restos a Pagar Processados :')

                print(f'segurança = {IRPP[0]}\nassistencia social = {IRPP[1]}\nprevidencia social = {IRPP[2]}\nsaúde = {IRPP[3]}\neducação = {IRPP[4]} ')

    except:
        return 'pinto'
            

#------------------------------------------- Executando :

Estado_Desejado = input('digite o estado que você procura >>')  
#State_Statistics(Table,Estado_Desejado)
#falta implementar a sumlist

Municipio_Statistics(Table,Estado_Desejado)