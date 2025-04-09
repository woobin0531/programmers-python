def solution(n):
    import math
    lcm = n * 6 // math.gcd(n, 6)
    return lcm // 6