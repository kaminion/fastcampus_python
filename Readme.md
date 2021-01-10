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