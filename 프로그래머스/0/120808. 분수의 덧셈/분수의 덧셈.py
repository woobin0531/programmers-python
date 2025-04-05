import math  # 최대공약수 계산을 위해 math 모듈 사용

def solution(numer1, denom1, numer2, denom2):
    # 분수 덧셈: 공통 분모를 이용하여 계산
    numer = numer1 * denom2 + numer2 * denom1  # 분자 계산
    denom = denom1 * denom2  # 분모 계산
    
    # 기약 분수로 만들기 위해 최대공약수(GCD) 계산
    gcd = math.gcd(numer, denom)
    
    # 최대공약수로 나누어 기약 분수로 변환
    return [numer // gcd, denom // gcd]
    