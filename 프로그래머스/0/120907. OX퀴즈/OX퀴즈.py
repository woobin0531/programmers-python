def solution(quiz):
    answer = []
    for q in quiz:
        x, op, y, eq, z = q.split()
        
        x = int(x)
        y = int(y)
        z = int(z)

        if op == "+":
            result = x + y
        elif op == "-":
            result = x - y

        if result == z:
            answer.append("O")
        else:
            answer.append("X")
    return answer