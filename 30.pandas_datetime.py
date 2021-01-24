import pandas as pd

df = pd.read_csv('./data/korean-idol.csv')
# 현재 생년월일은 object 타입으로 저장되어있음(문자열)
#print(df['생년월일'])

#to_datetime() 메서드 사용해서 날짜 데이터로 바꿔줌
df['생년월일'] = pd.to_datetime(df['생년월일'])
print(df['생년월일'])

# DatetimeProperties Object의 속성을 사용 가능
print(df['생년월일'].dt)

#연월일 추출가능 weekofyear, dayofweek 같은것도 사용가능
print(df['생년월일'].dt.year)