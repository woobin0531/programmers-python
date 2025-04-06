def solution(array):
    array.sort()
    i = len(array)//2
    answer = array[i]
    return answer
    
    
                      #1, 3, 5, 7, 9  --> 5개  5개를 2 로 나누면 2.5 0.5 없애고 +1
    