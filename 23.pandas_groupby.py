import pandas as pd
df = pd.read_csv('./data/korean-idol.csv')

# 데이터를 그룹으로 묶어 분석할 때 활용함


# 출력이 되지 않는 이유는 그룹만 묶어놓은 상태이기 떄문이다!
print(df.groupby('소속사'))

# 함께 사용해야하는것 count(), sum(), mean()평균, var()분산, std()표준편차, min()/max()

#print(df.groupby('성별').mean())
# 특정 column만 추출가능 
print(df.groupby('성별')['키'].mean())