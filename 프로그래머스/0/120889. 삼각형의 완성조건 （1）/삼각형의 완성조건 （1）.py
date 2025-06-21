def solution(sides):
    sides.sort()  # 길이를 오름차순으로 정렬
    if sides[2] < sides[0] + sides[1]:
        return 1  # 삼각형을 만들 수 있음
    else:
        return 2  # 삼각형을 만들 수 없음

    