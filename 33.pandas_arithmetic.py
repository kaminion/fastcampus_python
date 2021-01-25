import pandas as pd
import numpy as np

df = pd.DataFrame({'통계':[80, 70, 80, 50, 79], '미술':[50, 60, 70, 88, 30], '체육':[50, 60, 70, 88, 90]})
print(df)

# column 간 연산(Series 간의 연산) 같은 인덱스 끼리 덧셈함
print(df['통계'] + df['미술'] + df['체육'])

# column 과 숫자간 연산 (Broadcasting) 맞게 자연스럽게 나옴 
print(df['통계'] + 10)

# 복합 연산 (공식 명칭은 아님)
print(df['통계'] + df['미술'] + 10)

# mean
print(df.mean(axis=1)) # axis 0이면 행, 1이면 열에 대한 평균

print(df.sum(axis=0))

# NaN값이 존재할 경우 연산
df2 = pd.DataFrame({'통계':[80, 70, np.NaN, np.NaN, 79], '미술':[50, np.NaN, 70, 88, 'okay'], '체육':[np.NaN, 60, 70, 88, 90]})
print(df2['통계'] + 2) # NaN 연산은 NaN값만 남음

# DataFrame과 DataFrame간 연산
# 연산이 불가능한 문자열 있으면 자동으로 에러 발생
#print(df + df2)

# column의 순서가 다른경우

df3 = pd.DataFrame({'통계':[80, 70, 80, 50, 79], '체육':[50, 60, 70, 88, 30], '미술':[50, 60, 70, 88, 90]})
df4 = pd.DataFrame({'미술':[80, 70, 80, 50, 79], '통계':[50, 60, 70, 88, 30], '체육':[50, 60, 70, 88, 90]})

#알아서 column 순서 맞춰서 삽입
print(df3 + df4)

# 행의 수가 다른 경우 알아서 NaN값 할당