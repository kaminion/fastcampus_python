import pandas as pd

df = pd.read_csv('http://bit.ly/ds-korean-idol')

# 객체 주소가 복사되므로
new_df = df.copy()
new_df['이름'] = 0

print(df.head())