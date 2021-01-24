# 병합하기
# 단순 합치는 것과는 결이 다르다.
# concat : row와 column 기준으로 단순 이어 붙이기
# merge : 특정 고유한 키(unique id) 기준으로 합침

import pandas as pd

df = pd.read_csv('./data/korean-idol.csv')
df2 = pd.read_csv('./data/korean-idol-2.csv')
# 두 column 중에 이름이 겹친다.
#print(df, df2)

# 이름 기준으로 merge

# 이 상태에서 concat하면 데이터가 맞지않음
df_right = df2.drop([1, 3, 5, 7, 9], axis=0)

df_right = df_right.reset_index(drop=True)

# on에는 기준이 되는 column을 넣어줌, how는 left, right, inner, outer
# how에 left 지정해주면 left 기준으로 들어감, right 데이터 프레임 값이 없으면 NaN값 들어감
print(pd.merge(df, df_right, on="이름", how="left"))

# 만약 how가 right라면 right에는 없는 값들을 드랍시켜버린다.
print(pd.merge(df, df_right, on="이름", how="right"))

# inner(교집합) outer(합집합) 어떻게보면 left, right와 똑같다.

# 만약 이름과 성함같은 비슷한 성질의 컬럼이 있다면? (이걸 기준으로 합쳐도 무방하다면?)
# 이럴 때는 pd.merge(df, df_right, left_on="", right_on="", how="") 가 가능하다.