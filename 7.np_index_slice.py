import numpy as np

# 슬라이싱의 경우 list에도 공통으로 적용된다

# 1차원 arr
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

print(arr.shape)

# index 지정하여 색인

print(arr[-10])


# 2차원 arr 
arr2d = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])
print(arr2d.shape)

print(arr2d[0, 1])


# 범위 색인 (slicing)
# 1 이상 끝까지
print(arr[1:])

# index 5 미만
print(arr[:5])

# 1이상 5미만
print(arr[1:5])

# -1 전까지
print(arr[:-1])

# row(행)을 모두 가져오려는 경우
print(arr2d[0, :])

# column을 모두 가져오려는 경우
print(arr2d[:, 2])

# 부분적으로 가져오려는 경우

print(arr2d[:2, :])