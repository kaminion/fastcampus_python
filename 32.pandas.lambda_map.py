import pandas as pd
df = pd.read_csv('./data/korean-idol.csv')

# lambda의 적용
# 남자는 1로 여자는 0으로 바꿈
df['성별'] = df['성별'].apply(lambda x : 1 if x == "남자" else 0)

print(df)


# map은 반드시 dict 타입이어야 함. key는 바꾸어야 할 값, value는 바꿔질 값
my_map = {
    1 : 'male',
    0 : 'female'
}

#map 적용
df['성별'] = df['성별'].map(my_map)
print(df)