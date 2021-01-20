import pandas as pd

df = pd.read_csv('./data/korean-idol.csv')

# 통계값 다루기

# 계략적인 통계값 확인가능 (수치형 데이터인 int와 float만 나타냄)
print(df.describe())   
# mean 평균
# std 표준 편차 : 얼마만큼 평균값으로부터 데이터들이 떨어져있는가를 나타내는 지표


print(df.head())

# 해당 컬럼을 추출하면 Series 데이터인데, 여기에 메서드를 사용
print(df['키'].min(), df['키'].max())

# 분산과 표준 편차
# 분산과 표준편차는 데이터가 평균으로부터 얼마나 떨어져 있는지 정도를 나타낸다.
# var, variance(분산) / std, standard deviation
# 분산 : (데이터- 평균)**2(제곱)을 모두 합한값에 평균으로 나눔
# 표준 편차는 분산의 루트

import numpy as np

data_01 = np.array([1, 3, 5, 7, 9])
data_02 = np.array([3, 4, 5, 6, 7])

# 값이 같다고 데이터의 성격이 같진 않다.
print(data_01.mean(), data_02.mean())

# 그래서 분산을 찍어본다. 분산이 크면 더 데이터가 넓게 떨어져있음을 볼 수 있다.
print(data_01.var(), data_02.var())

# sqrt(루트), 분산에 루트를 적용, 보통은 표준 편차값으로 사용함(std)
# 데이터가 커지면 분산 값이 커져서 알아볼 수 없으므로 보통은 표준 편차값으로 확인한다.
print(np.sqrt(data_01.var()), np.sqrt(data_02.var()))


# 직접 분산과 표준편차 구하기
# 분산 ((데이터의 값 - 평균) 제곱) / 평균
standard_deviation = ((3-5) ** 2 + (4-5) ** 2 + (5-5) ** 2 + (6-5) ** 2 + (7-5) ** 2) / 5
print(standard_deviation)

# 개수를 세는 count
print(df['키'].count())

# 중앙값은 오름차순으로 정렬한 후 가장 가운데 있는 값을 매김(홀수개는 가장 가운데, 짝수는 가운데 앞뒤값의 평균 혹은 앞뒤값들중 임의로 하나 )
print(df['키'].median())

# 최빈값(mode) 제일 많이 출현하는 값
print(df['키'].mode())
