# 데이터 시각화
# 데이터가 많을 경우 필요하다.
# EDA 할 때 필요
# EDA(Exploratory Data Analysis) 탐색적 데이터 분석 : 수집한 데이터가 들어왔을 때 이를 다양한 각도에서 관찰하고 이해하는 과정
import pandas as pd

df = pd.read_csv('./data/house_price_clean.csv')
print(df)
df.plot() # 주피터 노트북에선 그래프가 나온다.

# 시각화 라이브러리
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm 

# 아래부분은 코랩 한글 설정 (이거 설정하고 런타임 재시작)
# !apt-get -qq -y install fonts-nanum > /dev/null
fontpath = '/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf'
font = fm.FontProperties(fname=fontpath, size=10)
fm._rebuild()

# %config inlineBackend.figure_format = 'retina'
plt.rc('font', family="NanumBarunGothic")
# 여기까지 설정

# Graph 사이즈 키우는 옵션
plt.rcParams['figure.figsize'] = (12, 9)
print(df.plot())

df['분양가'].plot()

#kind 옵션을 통해 원하는 그래프를 그릴 수 있다.
df['분양가'].plot(kind='line')

df_seoul = df.loc[df['지역'] == "서울"]
print(df_seoul)
df_seoul_year = df_seoul.groupby('연도').mean()
print(df_seoul_year)
# line 그래프는 데이터가 연속적인 경우 사용하기 적절하다.
print(df_seoul_year.plot(kind='line'))

# bar 그래프는 그룹별로 비교할 때 유용하다.
df.groupby('지역')['분양가'].mean().plot(kind='bar') # 가로 그래프를 보려면 barh 옵션을 주면 된다.

# histogram 분포 - 빈도를 시각화하여 보여줌, 도수 분포표라고도 한다.
# 가로축에는 분포를, 세로축에는 빈도를 시각화하여 보여준다.
df['분양가'].plot(kind='hist')