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

# 커널 밀도 그래프
# 히스토그램과 유사하게 밀도를 보여주는 그래프
# 히스토그램과 유사한 모양새 (히스토그램은 막대, 얘는 유선형 그래프)
# 부드러운 라인을 가지고 있다.

df['분양가'].plot(kind='kde')

# Hexbin
# 고밀도 산점도 그래프 (X와 Y축 을 비교해서 밀도가 얼마나 되는지)
# x와 y 키값을 넣어주어야함
# x, y 모두 numeric한 값 을 요구함
# 데이터의 밀도를 추정함

#xx = df.loc[(df['분양가'] > 1000) & (df['분양가'] < 2000)]
df.plot(kind='hexbin', x='분양가', y='연도', gridsize=20) # size를 정의해주어야 크게 보임

# 박스 플롯
df_seoul = df.loc[df['지역'] == '서울']
df_seoul['분양가'].plot(kind='box')

from IPython.display import Image

Image('https://justinsighting.com/wp-content/uploads/2016/12/boxplot-description.png')
# Possible Outliers : 
# Upper Whisker : 최대값
# 3rd Quartile : 4분의 3 지점
# median : 해당값의 중앙값
# 1st Quartile : 4분의 1 지점
# Lower Whisker : 최소값

df_seoul.describe()
# 실제 최솟값과 최대값이 아니고 이걸 넘어가는 값을 Outlier라고 한다.
# IQR 는 INTER Quartile Range의 약어로, (3Q - 1Q) * 1.5 값이다. ( 75% - 25% )* 1.5 


# area plot은 line 그래프에서 아래 area를 모두 색칠해주는 것이 특징이다.

df.groupby('월')['분양가'].count().plot(kind='line')
df.groupby('월')['분양가'].count().plot(kind='area')

# pie plot(파이 그래프)
# 데이터의 점유율을 보여줄 때 유용하다.
df.groupby('연도')['분양가'].count().plot(kind='pie')

# scatter plot(산점도 그래프)
# 점으로 데이터를 표기해줌
# x, y 값을 넣어주어야함 (hexbin과 유사)
# numeric한 column만 지정가능
# X축과 Y축 비례관계, 시계열 데이터들 X축은 연도, Y축은 물가일 경우 산점도에서 Linear한 관계를 보여줄 수 있다. (분포도 추세를 볼 수 있음.)
df.plot(x='월', y='분양가', kind='scatter')