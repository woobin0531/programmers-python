from collections import Counter

def solution(s):
    counter = Counter(s)  
    one_time_chars = [char for char in counter if counter[char] == 1]
    return ''.join(sorted(one_time_chars))
