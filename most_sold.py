import pandas as pd

def desafio4MostSold(parquet_file='./sales.parquet'):
    df = pd.read_parquet(parquet_file, engine='auto')
    idmax = df['sales'].idxmax() #maximo de una columna, devuelve id
    print("Maximo de ventas: " + str(df.ix[idmax]['sales']))
    print("Item: " + df.ix[idmax]['title'] + " - ID: " + df.ix[idmax]['item_id'])

desafio4MostSold()