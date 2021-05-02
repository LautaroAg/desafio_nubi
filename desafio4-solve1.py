import pandas as pd
import csv
from sys import exit
#  Python 2 porque no pude instalar pyarrow para python3
def  desafio4Solve1(
    parquet_file='./sales.parquet',
    currencies_file='./currenciesClean.csv',
    conversion_rate='local_to_dollar' # acepta dolar_to_local
    ):
    """
    Resuelve el desafio 4
    """
    conv_index = 3 if conversion_rate == 'local_to_dollar' else 2
    df = pd.read_parquet(parquet_file, engine='auto')

    with open(currencies_file,'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        csv_dict = {} 
        for row in csv_reader:
            csv_dict[row[2]] = row[1::conv_index] # currency id : date, local to dollar
        conversion_rate_list = []

        for row in df.iterrows():        
            if csv_dict[str(row[1]['currency_id'])][0] == (row[1][u'date']):
                conversion_rate_list.append(csv_dict[str(row[1]['currency_id'])][1])
            else:
                exit("No hay informacion para el dia: " + str(row[1][u'date']))

        df[conversion_rate] = conversion_rate_list

        print(df[['currency_id',conversion_rate]])
        print(df.columns)

desafio4Solve1(conversion_rate='dolar_to_local')