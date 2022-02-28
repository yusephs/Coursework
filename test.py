import pandas as pd

df = pd.read_csv('data2.csv', sep='|')

print(df.to_string()) 