"""
    < while 문 >
    형식:
        while 조건식:
            조건문이 True 일 동안 반복할 문장들 (종속문장)


    * 순서 :
        조건식 실행
        ↑   └--- True  ---> 종속문장 실행   -----┐
        │   └--- False ---> while문 종료         │
        └---------------------------------------┘

"""

n = 1
while n <= 10:
    print(n)
    n += 1
print(f'마지막 n : {n}')
# 결과
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 마지막 n : 11
