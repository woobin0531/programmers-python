def solution(my_string):
    result = ''
    for ch in my_string:
        if ch not in result:
            result += ch
    return result
