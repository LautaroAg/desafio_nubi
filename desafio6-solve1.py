import pandas as pd


def desafio6Solve1(parquet_file='./joinedWithRowKey.parquet'):
    """
    Resuelve el desafio 6
    """
    data_dict = {}
    df = pd.read_parquet(parquet_file, engine='auto')
    for i in range(1,8):
        for row in df.iterrows():
            level = 'level' + str(i)
            level_id = str(row[1][level])
            try:
                data_dict[(level,level_id)] += row[1]['sales']
            except:
                data_dict[(level,level_id)] = 0
    data_final = {'level':[],'level_id':[],'sales':[]}
    for data_key in data_dict.keys():
        data_final['level'].append(data_key[0])
        data_final['level_id'].append(data_key[1])
        data_final['sales'].append(data_dict[data_key])
    print(data_final)
    df_new = pd.DataFrame(data_final)
    df_new.to_parquet('./levels.parquet')
    
desafio6Solve1()