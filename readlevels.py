import pandas as pd

df = pd.read_parquet('./levels.parquet', engine='auto')

for row in df.iterrows():
    print(row)
