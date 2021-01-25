import pandas as pd

df = pd.read_csv('./data/korean-idol.csv')

print(df.info())

# 데이터분석에 많이 사용함
# 데이터 타입별로 column을 선택할 수 있음 
# include는 포함, exclude는 배제하고 검색
print(df.select_dtypes(include="object"))
print(df.select_dtypes(exclude="object")) # 산술통계에 연산 적용 가능

# column 명만 받아오기
num_cols = df.select_dtypes(exclude="object").columns
print(num_cols)
print(df[num_cols]) # 컬럼들을 모두 조회