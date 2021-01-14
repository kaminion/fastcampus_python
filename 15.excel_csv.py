# CSV 파일
# Comma Separated Value의 약어로써, 쉼표로 구분된 파일
# 엑셀보다 가볍다
import pandas as pd

csvfile = pd.read_csv('./data/korean-idol.csv')
print(csvfile)

excelfile = pd.read_excel('./data/korean-idol.xlsx')
print(excelfile)