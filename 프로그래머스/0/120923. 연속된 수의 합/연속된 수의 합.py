def solution(num, total):
    start = (total - (num * (num - 1) // 2)) // num
    return [i for i in range(start, start + num)]