# 단순하게 데이터 붙이기
# 특정 기준 없이 단순 붙이기만 함
import pandas as pd

# 국내 아이돌 평판지수  https://bit.ly/ds-korean-idol
df = pd.read_csv('./data/korean-idol.csv')
# 국내 아이돌 연봉 가족수 https://bit.ly/ds-korean-idol-2
df2 = pd.read_csv('./data/korean-idol-2.csv')

#print(df.head())

df_copy = df.copy()
# print(df_copy)

# row 기준으로 합칠 땐 list 로 합쳐주고, sort=False 옵션을 주어 순서가 유지되도록 한다.
df_concat = pd.concat([df, df_copy], sort=False)
print(df_concat) 
# 행 인덱스가 겹친상태로 합쳐져 인덱스를 초기화해줌
df_concat = df_concat.reset_index(drop=True)
# 기존 인덱스 컬럼을 보존하기때문에 삭제하라는 option을 넣어줌
print(df_concat)

# column 기준으로 합치기
# print(df2) 
#axis 옵션만 1로 바꿔주어 열기준으로 합친다.
df_concat2 = pd.concat([df, df2], axis=1)
# 단순하게 합쳐진 결과를 확인가능
print(df_concat2)

df3 = df2.drop([3, 5])
# 데이터의 갯수가 맞지 않을때 합쳐지면 자동으로 NaN값으로 채움
# 인덱스 기준으로 합쳐짐
df_concat3 = pd.concat([df, df3], axis=1)
print(df_concat3)