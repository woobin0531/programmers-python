def solution(my_string):
    vowels = 'aeiou'
    result = ''
    for ch in my_string:
        if ch not in vowels:
            result += ch
    return result
