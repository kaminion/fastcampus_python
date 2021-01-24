import pandas as pd


# apply는 series나 dataframe에 좀 더 구체적인 로직을 적용하고 싶은 경우 활용

# ex ) 남자는 1, 여자는 0으로 바꾸고 싶을 경우
df = pd.read_csv('./data/korean-idol.csv')

# df.loc[(df["성별"] == "남자"), "성별"] = "1"
# df.loc[(df["성별"] == "여자"), "성별"] = "0"

# print(df)


def male_or_female(x):
    if x == "남자":
        return 1
    elif x == "여자" :
        return 0

df['성별'] = df['성별'].apply(male_or_female)
print(df['성별'])


# 키의 cm당 브랜드 평판지수 구하기 ( 브랜드 평판지수 / 키 )
# 단일 series가 아닌 dataframe 통채로 넘겨줌
def cm_to_brand(df):
    value = df['브랜드평판지수'] / df['키']
    return value

# axis 0은 행은 사라지고 열단위 집계 1 옵션을 주게 되면 행단위 집계를 함.
# series에는 해당 옵션이 expect 값이 아님.
df['cm_to_brand'] = df.apply(cm_to_brand, axis=1)
print(df)