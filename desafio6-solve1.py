import pandas as pd


def desafio6Solve1(parquet_file='./joinedWithRowKey.parquet'):
    """
    Resuelve el desafio 6
    """
    dict_new = {}
    df = pd.read_parquet(parquet_file, engine='auto')
    for i in range(1,8):
        for row in df.iterrows():
            level = 'level' + str(i)
            level_id = str(row[1][level])
            try:
                dict_new[(level_id,level)] += row[1]['sales']
            except:
                dict_new[(level_id,level)] = 0
    

    #data = [(key[1] , key[0], dict_new[(key[0],key[1])]) for key in dict_new.keys()]
    #print(data)
    df_new = pd.DataFrame(data, columns=['level', 'level_id', 'sales'])
    df_new.to_parquet('./levels.parquet')
    
desafio6Solve1()