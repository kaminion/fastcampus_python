# Series Type 변환
# 각각의 series (열, 컬럼) 별로 타입을 확인하는 것이 중요하다.
# 보통 타입은 아래와 같다.
# object : 일반문자열
# float : 실수
# int : 정수
# category : 카테고리
# datetime : 시간

import pandas as pd

df = pd.read_csv('./data/korean-idol.csv')

# type 확인하기 
print(df.info())

# 먼저 컬럼의 타입 확인(Series)
print(df['키'].dtypes)

# astype이라는 메서드로 타입 변경가능하다. (Series별로만 가능)

# 결측치 채우기
df['키'] = df['키'].fillna(-1)
print(df['키'])
print(df['키'].astype(int)) # 결측데이터가 있을 경우 정수형 변경X