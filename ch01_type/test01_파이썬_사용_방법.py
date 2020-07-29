"""
    1. Python 명령은 가장 윗줄부터 아래 방향으로 진행한다.
        중간에 에러가 발생한 경우 그 다음 행은 실행되지 않는다.
        들여쓰기(tab, 맨 앞 공백) 또한 명령의 일종이므로 일반 명령어 앞에는 들여쓰기하지 않는다.
        코드 한 행이 명령어 1개다.

    2. 모든 텍스트는 명령으로 인식된다.
        따라서 메모(=주석, comment)를 해야하는 경우
        # : 한 줄 주석
        쌍따옴표3개씩 : 문단 주석
        이 두가지 방법을 사용해야 한다.

        단축키 : 주석 처리할 문단 드래그 > ctrl + '/'

    3. 결과를 출력하고 싶다면 print() 명령을 사용한다.
    4. 저장은 ctrl + S를 사용하지만 파이참은 자동 저장 기능을 제공한다. (기본 15초 간격)
    5. 실행은 ctrl + shift + F10
        하단의 run 창이 실제 cmd 창이라고 보면 된다.
        실제로 실행을 하면 다음과 같은 결과를 볼 수 있다.
    -------------------------------------------------------------------------------------------------------
    C:/Python/python.exe C:/Users/issel/PycharmProjects/Python_tutorials/ch01_type/test01_파이썬_사용_방법.py

    ( 이 부분이 실제 결과 )

    Process finished with exit code 0
    -------------------------------------------------------------------------------------------------------
     ** 15번 줄은 cmd 에서 확인했던 'python 파일명.py'의 절대경로를 사용한 방식이다.
     ** exit code 0 의 의미는 '정상 종료'를 의미한다.
        1) 이 텍스트가 보이면 해당 테스트는 종료된 것으로 보면 된다.
            안보이면 테스트 프로그램은 실행 중이란 뜻!
        2) 비정상 종료인 경우 0이 아닌 다른 값을 반환한다.

    6. cmd, terminal, 명령 프롬프트는 모두 같은 의미로 사용된다.
"""