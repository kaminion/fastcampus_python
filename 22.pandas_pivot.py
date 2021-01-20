import pandas as pd
import numpy as np

# 피벗테이블(pivot_table)
# 엑셀의 피벗테이블과 동일하다
# 여러개의 열 중에서 두개를 뽑아서 각각 행 인덱스, 열인덱스로 사용하여 데이터를 조회하여 펼쳐놓은것
# 좌측 인덱스
df = pd.read_csv('./data/korean-idol.csv')

# index 행 인덱스로 지정할 column, columns="별로" values="궁극적으로 조회하려는 값", index와 columns는 분류기준이라고 볼 수 있음.
print(pd.pivot_table(df, index="소속사", columns="혈액형", values="키")) # 중복값이 있을경우 해당값의 평균값을 나타냄

#aggfunc는 추가 계산옵션 - 기본적으로 평균값을 나타내는 것이 불만이라면 aggfunc를 넣어줌 np.sum, np.mean 평균과 합계를 넘파이의 함수 사용으로 구할 수 있음 
# [] 리스트 형태로 넣을수도 있다
print(pd.pivot_table(df, index="소속사", columns="혈액형", values="키", aggfunc=np.sum))