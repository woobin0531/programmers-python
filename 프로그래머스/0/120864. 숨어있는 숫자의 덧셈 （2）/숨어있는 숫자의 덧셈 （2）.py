def solution(my_string):
    num = ''     # 숫자를 이어붙일 임시 문자열
    total = 0    # 최종 합계

    for ch in my_string:
        if ch.isdigit():         # 숫자라면
            num += ch            # 이어붙이기
        else:
            if num:              # 지금까지 모아둔 숫자가 있으면
                total += int(num)
                num = ''         # 다시 초기화
    if num:                      # 마지막 숫자가 남아있을 경우
        total += int(num)

    return total
