# List만 사용할 수 있다.
mylist = [1, 2, 3, 4, 5, 6, 7]

even = []

# 기존 코드
for i in mylist:
    if i % 2 == 0:
        even.append(i)
print(even)

# list comprehesion을 사용할 경우
# 맨 앞 변수가 결과값(새로 변수에 담기는 값, 뒤에꺼부터 해석 후 리턴되는 변수라고 생각하면 된다.)
newEven = [ i for i in mylist if i % 2 == 0]
print(newEven)

# 모든 리턴되는 변수에 + 2 더하기
plusList = [i + 2 for i in mylist if i % 2 == 0]
print(plusList)