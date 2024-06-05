import pandas as pd

url = 'https://raw.githubusercontent.com/DaThabor/Data-Training/master/Source%20Files/WideWorldImports%20csv/Application_Cities.csv?token=GHSAT0AAAAAACSUBNVBALES6MJM5MHRLF72ZS77FCQ'
df = pd.read_csv(url)
print(df.head(5))