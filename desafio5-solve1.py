import pandas as pd

def desafio5Solve1(parquet_file='./joined.parquet', output='./joinedWithRowKey.parquet'):
    """
    Resuelve el desafio 5 guardando el resultado en el archivo recibido como parametro
    o el default: 'joinedWithRowKey.parquet'
    """
    
    df = pd.read_parquet(parquet_file, engine='auto')
    new_column = []
    for row in df.iterrows():
        new_column.append(row[1]['date']+'-'+row[1]['category_id'])
    df['row_key'] = new_column
    df.columns = [str(col) for col in df.columns] # pasa los nombres a String para poder guardar como .parquet
    df.to_parquet(output, engine='auto')

desafio5Solve1()
