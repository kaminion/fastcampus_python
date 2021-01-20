import pandas as pd

# 멀티인덱스

# 행 인덱스를 복합적으로 구성하고 싶은 경우 인덱스를 리스트로 만들어줌 
# 레벨이 
df = pd.read_csv('./data/korean-idol.csv')

# 처음꺼로 분류한 다음에 그 다음껄로 분류함
df2 = df.groupby(['혈액형', '성별']).mean()
print(df2)
# 피벗 테이블로 변환
print(df2.unstack('혈액형'))

# 멀티인덱스를 원래 데이터 프레임으로 바꿔버림

print(df2.reset_index())

# 분류한 데이터의 ROW별로 조회가능, 2개 이상 조회시 튜플을 이용해 조회해야함
print(df2.loc[('A', '남자')])