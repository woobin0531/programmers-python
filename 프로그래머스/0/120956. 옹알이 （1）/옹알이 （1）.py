def solution(babbling):
    words = ["aya", "ye", "woo", "ma"]
    answer = 0

    for s in babbling:
        pos = 0
        prev = ""
        valid = True

        while pos < len(s):
            matched = False

            for w in words:
                if s.startswith(w, pos):
                    # 같은 단어 연속 사용 금지
                    if prev == w:
                        valid = False
                        break
                    prev = w
                    pos += len(w)
                    matched = True
                    break

            if not matched:
                valid = False
                break

        if valid:
            answer += 1

    return answer
