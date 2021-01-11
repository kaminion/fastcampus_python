import numpy as np

arr = np.array([1, 2, 3, 4], dtype=int)

print(arr)

mylist1 = [1, 2, 3, 4]
mylist2 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8]
]

arr1 = np.array(mylist1)
arr2 = np.array(mylist2)

# shape (4,) = 4열
print(arr1.shape)

# shape (2, 4) 2행 4열
print(arr2.shape)

mylist3 = [[
    [1, 2, 3, 4],
    [1, 2, 3, 4],
],
[
    [ 1, 2, 3, 4],
    [1, 2, 3, 4]
]]

# shape (2, 2, 4) X 2 Y 2 Z 4 3차원 2개짜리 2행 2열
arr3 = np.array(mylist3)
print(arr3.shape)

# array에서는 list와는 다르게 1개의 단일 데이터 타입만 허용됨
arr = np.array([1, 2, 3, 4, 5.14]) # 정수가 강제로 실수형으로 캐스팅 됨
print(arr)

# 실수가 강제로 캐스팅됨
arr = np.array([1, 2, 3, 4, 5.14], dtype=int)
print(arr)

# int와 str 타입이 혼재 된 경우
arr = np.array([1, 3.14, '테디', '1234']) # 강제로 문자열로 캐스팅됨
print(arr)

# int와 str 타입이 혼재 되어있고 dtype을 int로 지정하면 캐스팅 에러가 난다.