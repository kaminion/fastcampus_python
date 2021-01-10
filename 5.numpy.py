import numpy as np
# numpy 배열

# 1차원 numpy 배열
np.array([1, 2, 3, 4])

# 2차원 numpy 배열 
# nd array라고함 n-차원 배열
np.array([[1,2,3,4,5], [1,2,3,4,5]])

# shape의 개념 중요!
# shape은 차원으로 갯수가 나옴, 표시되는 값들은 row부터(x부터) 계산, 
# (3, ) => 3 X 1의 배열 X 1차원
# (4, 3) => 4 X 3 의 배열 X Y 2차원
# (2, 5, 3) => 2 X 5 X 3 의 배열 X Y Z 3차원

# axis는 기준이 되는 축임. 행부터 계산 (0, 1, 2 순서로...)
# axis 0은 x
# axis 1은 y
# axis 2는 z