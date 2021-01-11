import numpy as np

# 순차적인 값을 생성해주는것

# arange를 사용해서 쉽게 생성가능
# 첫번쨰 인자는 start 이상, 두번째는 stop 미만
arr = np.arange(1, 11)
print(arr)

# 함수 호출 시 keyword 인자 활용가능
arr = np.arange(stop=11, start=1)
print(arr)

arr = np.arange(1, 11, 2)
print(arr)