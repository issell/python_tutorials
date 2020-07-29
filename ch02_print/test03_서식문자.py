"""

    < 서식문자(Format characters) >
    - 값을 '서식'에 맞추는 문자열
    - % + 문자
    - '서식문자가 포함된 문자열' % (값1, 값2, ..)

    < 주요 서식문자 >
    %i : integer (정수)
    %d : decimal (10진수 정수)
    %o : octal (8진수 정수)
    %h : hexadecimal (16진수 정수)
    %f : float (실수)
    %lf : long float (실수)
    %s : string (문자열)
    %c : character (단일문자)

"""

s1 = '나는 %s이다.' % '홍길동'
s2 = '나는 %s이고, %d 살이다.' % ('홍길동', 15)
s3 = '나의 키는 %f이다.' % 168.2
s4 = '나의 키는 %.2f이다.' % 168.2

print(s1)  # 나는 홍길동이다.
print(s2)  # 나는 홍길동이고, 15 살이다.
print(s3)  # 나의 키는 168.200000이다.
print(s4)  # 나의 키는 168.20이다.


kr = 88
en = 80
ma = 67
goal_grade = 'B'
print('국어 %d점, 영어 %d점, 수학 %d점' % (kr, en, ma))
print('총점은 %d점, 평균은 %.1f 점이다.' % (kr + en + ma, (kr + en + ma) / 3))
print('%c 학점을 넘었으면 좋겠다!' % goal_grade)
# 국어 88점, 영어 80점, 수학 67점
# 총점은 235점, 평균은 78.3 점이다.
# B 학점을 넘었으면 좋겠다!

print("%d %o %x" % (0b100000, 0b100000, 0b100000))
# 32 40 20
