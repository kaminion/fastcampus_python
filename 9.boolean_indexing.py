import numpy as np

# 조건 필터링을 통하여 Boolean 값을 이용한 색인
# array[조건 필터]
arr2d = np.array([[1, 2, 3, 4],  [5, 6, 7, 8]])
# 결과값을 알아서 필터해줌 
print(arr2d[ arr2d > 2] )
# boolean 으로 리턴
print(arr2d > 2)