import pandas as pd 
# datanya dikit
df = pd.read_csv("data/Data.csv")
# untuk menampilkan semua data
pd.set_option('display.max_rows', None)
print(df)