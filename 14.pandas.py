# pandas
# 엑셀로 할 수 있는 모든 것들 가능
# DB핸들링 크롤링 엑셀 읽기 등..
import pandas as pd

# Series 1차원으로 이루어진 데이터 배열
# DataFrame 2차원으로 이루어진 데이터 배열 (Series가 모인거라고도 볼 수는 있다.)

#print(pd.Series([1, 2, 3, 4]))


# dataFrame

# 방법 1. list로 만들기
company1 = [['삼성', 2000, '스마트폰'],
            ['현대', 1000, '자동차'],
            ['네이버', 500, '포털']]
df1 = pd.DataFrame(company1)

# 제목 컬럼명 만들기, 컬럼 수를 맞춰서 만들어줘야함
df1.columns = ['기업명', '매출액', '제품']

# 엑셀과 굉장히 유사하게 출력됨
#print(df1)


# dict로 만들기 이 경우 컬럼명을 만들지 않아도 됨, column : row형태 
company1 = {
    '기업명' : ['삼성', '현대', '네이버'],
    '매출액' : [2000, 1000, 500],
    '업종' : ['스마트폰', '자동차', '포털']
}

df2 = pd.DataFrame(company1)
#print(df2)

# index를 특정 column으로 지정하기

df1.index = df1['기업명'] # 추후 강의에서 이야기
#print(df1)

print(df1['매출액'])