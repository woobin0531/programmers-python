def solution(num_list):
    even = 0  # 짝수 개수
    odd = 0   # 홀수 개수

    for num in num_list:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1

    return [even, odd]
