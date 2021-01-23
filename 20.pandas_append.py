import pandas as pd

df = pd.read_csv('http://bit.ly/ds-korean-idol')

# row 만들기
# dict type으로 append 반드시 ignore_index=True를 옵션으로 주어야함.
df = df.append({'이름':'테디', '그룹':'테디그룹',
'성별':'남자', '소속사':'끝내주는 소속사', '생년월일':'1970-01-01',
'키':195.0, '혈액형':'O', '브랜드평판지수':123456789
}, ignore_index=True)

print(df.tail())

# column 만들기 (initiallize, 어떤 조건을 내걸든 적용되지않음, replace는 예외인듯)
df['국적'] = False
#print(df.head())
# 초기화 후 넣어주어야 함, 3항 연산자같은것 사용 X
df.loc[df['이름']=='지드래곤', '국적'] = 'KOREA'

print(df[['이름','국적']].head())
