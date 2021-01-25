# 원 핫 인코딩
# 한 개의 요소는 True 나머지 요소는 False로 만들어주는 기법임.
import pandas as pd

df = pd.read_csv('./data/korean-idol.csv')

print(df.head())

# 기계학습에서 numeric하게 바꿔주어야 함
blood_map = {
    'A':0,
    'B':1,
    "AB":2,
    "O":3
}

df['혈액형_code'] = df['혈액형'].map(blood_map)
print(df.head())
# 값이 몇개인지
print(df['혈액형_code'].value_counts())

# 머신러닝에서 값들 간 관계를 잘못 적용할 수 있음( 다 독립적이지만 머신러닝은 numeric한 것을 관계지을 수 있음 )
# 하나만 1이고 나머지는 0, 즉 독립적인 존재임을 알려줄 수 있다. 산술연산에 의한 관계형성 X
print(pd.get_dummies(df['혈액형_code'], prefix="혈액형")) # prefix로 column 명 설정가능