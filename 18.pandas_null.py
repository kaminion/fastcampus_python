import pandas as pd

# 결측값(Null)
# DataFrame에서는 NaN => Not a Number 
df = pd.read_csv('./data/korean-idol.csv')

# print(df)
# print(df.info())

print(df.isna())