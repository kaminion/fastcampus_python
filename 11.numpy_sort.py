import numpy as np

arr = np.array([1, 10, 5, 6, 7, 8, 3, 2, 11])

print(np.sort(arr))

# 슬라이싱 옵션에 마지막 -1 내림차순 정렬
print(np.sort(arr)[::-1])

# 여태껏 유지가 되지 않았지만 자체적인 sort 메서드를 실행하면 유지됨
arr.sort()
print(arr)

# 편한 방식으로 사용

# N 차원 정렬

arr2d = np.array([[5, 6, 7, 8],
                  [4, 3, 2, 1], 
                  [10, 9, 12, 11]])

# 정렬 시 axis를 고려하여 정렬
print(arr2d.shape)

# 열 정렬
print(np.sort(arr2d, axis=1))

# 행 정렬 (위에서 아래로)
print(np.sort(arr2d, axis=0))
