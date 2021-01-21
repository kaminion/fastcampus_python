import pandas as pd
import numpy as np

df = pd.read_csv('./data/korean-idol.csv')

# 25에선 빈값(결측치)가 있는 열을 채워주었다.

# 빈 값이 있는 행을 제거
print(df.dropna(axis=0))
# 빈 값이 있는 열을 제거 (통째로 날림..)
print(df.dropna(axis=1))

# how 옵션 - any 한개라도 있는경우 드랍, all은 모두 NaN 인경우 드랍
print(df.dropna(axis=0, how="all"))

df.iloc[10] = np.nan
print(df.dropna(axis=0, how="all"))

# 중복값이 있는 행을 제거
df = pd.read_csv('./data/korean-idol.csv')

# keep 옵션으로 어떤값을 우선으로 남길지 정해줄 수 있다.
print(df['키'].drop_duplicates(keep="last"))

# 행 전체 중복을 검사
print(df.drop_duplicates('그룹'))