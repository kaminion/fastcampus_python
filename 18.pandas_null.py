import pandas as pd

# 결측값(Null)
# DataFrame에서는 NaN => Not a Number 
df = pd.read_csv('./data/korean-idol.csv')

# print(df)
# print(df.info())

# true나 false로 리턴 isna === isnull
print(df.isna()) # 빠진값인가? 라고 물어보는것

print(df['그룹'][df['그룹'].notnull()]) # print(df['그룹'][0]) 이런식으로 계산이 되므로 null아닌게..

# 그룹이 Null 이 아닌 것들의 키와 혈액형을 불러옴
print(df.loc[df['그룹'].notnull(), ['키', '혈액형']])

