def solution(my_string, letter):
    result = ""
    for char in my_string:
        if char != letter:
            result += char
    return result

    