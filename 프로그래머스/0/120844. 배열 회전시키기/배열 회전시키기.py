def solution(numbers, direction):
    if direction == "right":
        return [numbers[-1]] + numbers[:-1]
    else:  # direction == "left"
        return numbers[1:] + [numbers[0]]
