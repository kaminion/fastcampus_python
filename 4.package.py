from IPython.display import Image

# 함수들이 뭉쳐진 하나의 .py 파일에 이루어진 것을 모듈이라함.
# 여러 개의 모듈을 그룹화 하면 패키지가 된다.
# 패키지는 종종 라이브러리라고 불린다.

# 이건 colab이나 주피터노트북에서 실행해볼것
Image('http://pythonstudy.xyz/Images/basics/python-package.png')

# 모듈 import 하기
# import는 파이썬 모듈을 불러오는 법임.

# 별칭 사용하기
#import pandas as pd

# pandas 라는 패키지 안에서 DataFrame이라는 모듈을 불러온다.
# from (상위폴더) import (가져올 모듈)
from pandas import DataFrame as df

# alias 지정 시 기존 이름 못씀
df()