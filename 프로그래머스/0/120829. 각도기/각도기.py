def solution(angle):
    if angle == 180:
        print("평각")
        return 4
    elif angle == 90:
        print("직각")
        return 2
    elif 0 < angle < 90:
        print("예각")
        return 1
    elif 90 < angle < 180:
        print("둔각")
        return 3
