def solution(A, B):
    if len(A) != len(B):
        return -1

    rotated = A
    for i in range(len(A)):
        if rotated == B:
            return i
        rotated = rotated[-1] + rotated[:-1]
    return -1
