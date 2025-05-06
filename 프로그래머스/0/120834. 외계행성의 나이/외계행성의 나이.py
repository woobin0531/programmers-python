def solution(age):
    result = ''
    for ch in str(age):
        result += chr(ord('a') + int(ch))
    return result

