def solution(polynomial):
    terms = polynomial.split(" + ")
    x_sum = 0   
    const_sum = 0   

    for term in terms:
        if "x" in term:
            if term == "x":  
                x_sum += 1
            else:
                x_sum += int(term.replace("x", ""))
        else:
            const_sum += int(term)
    result = []
    if x_sum != 0:
        if x_sum == 1:
            result.append("x")
        else:
            result.append(f"{x_sum}x")
    if const_sum != 0:
        result.append(str(const_sum))

    return " + ".join(result)
