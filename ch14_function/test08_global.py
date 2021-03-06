"""

    함수 내에서 전역변수는 값 변경이 기본적으로 불가능하다.
     => 함수 내에서 전역변수를 수정하면 디버그와 유지보수가 매우 힘들어지기때문.

    하지만 global 선언을 하는 경우 전역변수 값 변경이 가능하다.

"""

a = 10  # 전역변수

def test1():
    a = 20  # 동명의 지역변수가 생성된다.
    print(f'a:{a}')


test1()  # a:20
print(f'a:{a}')  # a:10  (전역변수 a에 영향이 없다.)

########################################################################

def test2():
    global a  # 전역변수 a를 사용하겠다.
    a = 20  # 전역변수를 그대로 사용한다.
    print(f'a:{a}')


test2()  # a:20
print(f'a:{a}')  # a:20  (전역변수 a의 값이 test2()에 의해 변경되었다.)


