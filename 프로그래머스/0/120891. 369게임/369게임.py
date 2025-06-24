def solution(order):
    return sum(1 for digit in str(order) if digit in '369')
