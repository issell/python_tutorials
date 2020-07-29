"""
    < 다차원 리스트 >
    - 리스트를 원소로 하는 리스트

    2차원 리스트 : 1차원 리스트를 원소로 갖는 리스트
        [ [1,2,3], [4,5,6] ]

    3차원 리스트 : 2차원 리스트를 원소로 갖는 리스트
        [ [ [1,2,3], [4,5,6] ], [ [1,2,3], [4,5,6] ] ]

    4차원 리스트 : 3차원 리스트를 원소로 갖는 리스트
        [ [ [ [1,2,3], [4,5,6] ], [ [1,2,3], [4,5,6] ] ], [ [ [1,2,3], [4,5,6] ], [ [1,2,3], [4,5,6] ] ] ]

    ....

"""

a = [[1, 2, 3], [4, 5, 6]]
print(a)  # [[1, 2, 3], [4, 5, 6]]

print(a[0][0])  # 1
print(a[0][1])  # 2
print(a[0][2])  # 3

print(a[1][0])  # 4
print(a[1][1])  # 5
print(a[1][2])  # 6

print(len(a))  # 2  (a의 원소 개수는 2개)
print(len(a[0]))  # 3 (a[0]의 원소 개수는 3개 (원소 자체가 리스트))
print(len(a[1]))  # 3 (a[1]의 원소 개수는 3개 (원소 자체가 리스트))

# 다차원 리스트의 반복처리 (2차원 리스트는 이중 for 문을, 3차원 리스트는 삼중 for 문을 사용한다.)
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j])


# a = [[1, 2, 3], [4, 5, 6]] 는 다음과 같은 방법으로 표현할 수 있다.
a = [[1,   2,   3],  # [0]행
     [4,   5,   6]]  # [1]행
#    [0]열 [1]열 [2]열

