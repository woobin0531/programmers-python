import math
def solution(a, b):
    denominator = b // math.gcd(a, b)
    while denominator % 2 == 0:
        denominator //= 2
    while denominator % 5 == 0:
        denominator //= 5
    return 1 if denominator == 1 else 2