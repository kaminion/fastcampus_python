# 가상환경 설정법

- venv
자바스크립트의 패키지 관리라고 생각하면 된다.
설정법은 python -m venv 경로 
ex ) python -m venv ./venv 
현재 패키지에선 예제대로 생성해놓은 상태이다.
그후 Scripts 디렉토리로 이동하여 activate.bat을 실행한 뒤 패키지 설치하면 됨.
환경을 종료 할 시 deactivate.bat을 실행

# freeze
freeze 명령어로 설치된 라이브러리를 내보낼 수 있다.
pip freeze > requirements.txt

기록된 라이브러리들은
pip install -r requirements.txt 
명령어로 설치가 가능하다.

# 설치된 패키지
IPython

pandas


# 행렬 연산
덧뺄셈 요건 
- shape이 같아야함 (행렬)
- 같은 Position 끼리 연산 함
- 결과값도 같은 Shape임
~~~python
    [[1, 2, 3],
     [2, 3, 4]]

     + [[3, 4, 5],
       [1, 2, 3]]
~~~

# 곱셈 요건
맞닿는 Shape이 같아야함
2*3 행렬과 3*2행렬은 곱셈 가능
2*3 과 2*3 행렬은 곱셈 불가
결과 행렬의 크기는 맞닿는곳이 아닌 바깥쪽 값으로 결정됨
같은 인덱스를 곱하고 곱한것을 총합해줌