"""
    < if 문 >
    형식:
        if 조건식:
            조건문이 True 일때 실행할 문장들 (종속문장)

    * 종속문장은 들여쓰기로 표현한다. (tab 혹은 공백 4칸)

"""
age = int(input('나이 : '))

if age >= 20:
    print('성인입니다.')

print(f'당신은 {age}살입니다.')

"""
    15 입력 시 
        당신은 15살입니다.

    25 입력 시 
        성인입니다.
        당신은 25살입니다.
"""