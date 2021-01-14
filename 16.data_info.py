import pandas as pd

df = pd.read_csv('./data/korean-idol.csv')

# 열 출력하기
print(df.columns)
# df.columns = ['컬럼이름1'...] 현재 있는 컬럼수와 동일하다면 바꿔짐, 아니라면 error

# 범위성 index를 알려줌 range(행의 개수)
print(df.index)

# 행의 정보와 데이터타입을 알려줌, 빠진값과 data타입을 볼때 활용
print(df.info())

# 통계 정보 (산술 연산을 할 수 있는 column만 출력)
# print(df.describe())
# count 갯수, mean 평균, std 표준편차, min 최소, %는 상위 기준으로 해당하는 값들

# print(df.shape)


# 상위 5개 하위 5개 값만보기 (인자로 숫자 전달하면 그 숫자만큼만 출력함)
# print(df.head())
# print(df.tail())

# index 기준 정렬
# 정렬 하기 
#print(df.sort_index())

# 역정렬(내림차순)
#print(df.sort_index(ascending=False))

# 값을 기준으로 정렬도 옵션 똑같다. by가 어떤 값을 기준으로 하냐에 따라 인자
#print(df.sort_values(by='키', ascending=False))

# 복수정렬, 앞에꺼 먼저 계산 후 뒤에꺼는 중복일 경우 계산
print(df.sort_values(by=['키', '브랜드평판지수']))