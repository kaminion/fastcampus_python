import pandas as pd


df = pd.read_csv('./data/korean-idol.csv')

# 데이터 전처리에 많이 사용
# na = 밸류가 비어있는것 nan도 포함 결측치

print(df.info())

# 누락된 데이터를 -1로 채우기
print(df['키'].fillna(-1)) # 유지하려면 inplace=True 옵션 또는 채워준 값을 대입해주어야함

df2 = df.copy()

# 일반적으로는 아래방법보다는 다시 대입하는 방식을 더 많이 사용하고 추천함.
print(df2['키'].fillna(-1, inplace=True))

df3 = df.copy()
# 최빈값이나 평균값을 넣기도 함 
height = df3['키'].mean()
print(height)
print(df3['키'].fillna(height))