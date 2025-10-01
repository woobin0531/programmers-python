def solution(bin1, bin2):
    # 1. 이진수 문자열을 10진수 정수로 변환
    num1 = int(bin1, 2)
    num2 = int(bin2, 2)
    
    # 2. 두 10진수를 더함
    decimal_sum = num1 + num2
    
    # 3. 10진수 합을 다시 이진수 문자열로 변환하고 '0b' 접두사 제거
    answer = bin(decimal_sum)[2:]
    
    return answer