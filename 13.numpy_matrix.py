# 1. 행렬 덧셈
import numpy as np

a = np.array([[1, 2, 3],
              [2, 3, 4]])

b = np.array([[3, 4, 5],
             [1, 2, 3]])

# 같은 포지션 끼리 덧셈 진행
# print(a + b)

a = np.array([[1, 2, 3],
             [2, 3, 4]])

b = np.array([[1, 2],
             [3, 4],
             [5, 6]])
# shape 이 맞지 않으면 연산이 되지 않는다. (operand broadcast error)
# print(a.shape, b.shape)
# print(a + b)

a = np.array([[1, 2, 3],
             [2, 3, 4]])
# 행 기준으로 다음 행에 있는 행의 열들을 더해버림
#print(np.sum(a, axis=0))

# 열 기준으로 같은 행에 있는 열들을 더해버림
#print(np.sum(a, axis=1))

# 2. 뺄셈과 덧셈은 동일함


# 3. 곱셈
normalList = [[1, 2, 3],
             [2, 3, 4]]

bigList = [[3, 4, 5],
          [1, 2, 3]]

columnList = [[1, 2],
             [3, 4],
             [5, 6]]

# 일반 곱셈 (단순 곱셈, shape이 같을 때 같은 포지션 곱셈을 함)

a = np.array(normalList)
b = np.array(bigList)

#print(a.shape, b.shape)
#print(a * b)

# 행렬연산에서 말하는 것은 dot product임 내적 곱
# 맞닿은 곳이 다르다면 연산 되지 않음 (align error)
a = np.array(normalList)
b = np.array(columnList)

#print(np.dot(a, b)) # a.dot(b) 도 가능 np를 권장

"""
[0][0] = 1 * 1 + 2 * 3 + 3 * 5 = 22
[0][1] = 1 * 2 + 2 * 4 + 3 * 6 = 28
[1][0] = 2 * 1 + 3 * 3 + 4 * 5 = 31
[1][1] = 2 * 2 + 3 * 4 + 4 * 6 = 40
"""

# broadcasting
# 엑셀 시트에서 전체적으로 100이라는 값을 더하고싶을 때
# 엑셀 시트와 그거와 맞는 shape를 만든담에 매트릭스 연산?
# broadcasting을 이용하면 매우 쉽게 가능

a = np.array(normalList)
b = np.array(bigList)

# broadcasting은 행렬 원소 모두에 연산을 함(유용)
print(a + 3)
print(a * 3)
print(a / 3)
