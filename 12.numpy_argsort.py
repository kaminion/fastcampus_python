import numpy as np

arr2d = np.array([[5, 6, 7, 8], 
                 [4, 3, 2, 1], 
                 [10, 9, 12, 11]])

# 해당하는 것의 정렬 후 인덱스를 리턴함
print(np.argsort(arr2d, axis=1))

