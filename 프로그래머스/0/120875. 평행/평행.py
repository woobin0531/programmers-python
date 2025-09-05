def solution(dots):
    def slope(a, b):
        # 기울기 계산 (x차가 0이면 분모 0 방지 위해 float('inf') 사용)
        if a[0] == b[0]:
            return float('inf')
        return (a[1] - b[1]) / (a[0] - b[0])
    
    # 점들
    a, b, c, d = dots
    
    # 세 가지 경우만 체크
    if slope(a, b) == slope(c, d):
        return 1
    if slope(a, c) == slope(b, d):
        return 1
    if slope(a, d) == slope(b, c):
        return 1
    
    return 0
