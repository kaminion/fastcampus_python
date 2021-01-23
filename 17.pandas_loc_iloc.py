import pandas as pd

df = pd.read_csv('./data/korean-idol.csv')
print(df.head())

# column을 선택하는 방법 
print(df['이름'], df.그룹, df["소속사"])


# 범위 선택(range selection)
# 단순 index에 대한 범위 선택 (column이 아닌 행 기준)
#print(df['이름'][:3]) df[:3]


# loc 굉장히 많이 사용 (왼쪽은 행, 오른쪽은 열)
# print(df.loc[:, '이름'])

# 부분 선택
# print(df.loc[:, ["이름", "생년월일"]])

# print(df.loc[3:8, ["이름", "생년월일"]])
 
# 행은 2부터 5까지, 이름부터 생년월일 column 까지 (생년월일 전까지가 아닌 포함) Numpy와 다름
# print(df.loc[2:5, "이름":"생년월일"])

#iloc(position으로 색인)
# print(df.iloc[:, [0, 2]])
# iloc는 numpy와 동일하게 동작
#print(df.iloc[1:5, [0, 2]])


# boolean indexing 
# numpy에서 했던것과 동일 조건부 검색 시 boolean으로 리턴
#print(df['키'] > 180)

# 모든 컬럼을 출력하지 않으려면..

print(df[df['키'] > 180]['이름'])
print(df.loc[df['키'] > 180, '이름'])

# isin 을 활용한 색인, column 지정해서 조건부 추출 가능
my_condition = ['플레디스', 'SM']
print(df['소속사'].isin(my_condition)) # boolean 출력

print(df.loc[df['소속사'].isin(my_condition)])
