import numpy as np

# 범위가 아닌 특정 index 집합의 값을 선택하여 추출하고 싶을 때 활용한다.
arr = np.array([10, 23, 2, 7, 90, 65, 32, 66, 70])

# index 집합을 넣으면 해당 index 값들이 추출됨
print(arr[[0, 1, 2]])


arr2d = np.array([[1, 2, 3, 4, 5], 
                 [6, 7, 8, 9, 10]])
                 
print(f"back slicing : {arr2d[[0, 1], :]}") # 2차원 0번째 1번째, 뒤에 열은 모두를 가져옴 
print(f"front slicing : {arr2d[:, [0, 1, 2]]}") # 앞에 모든 차원, 뒤에 열은 0, 1, 2만