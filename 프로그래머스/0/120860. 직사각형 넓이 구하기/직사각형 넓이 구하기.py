def solution(dots):
    xs = [x for x, _ in dots]
    ys = [y for _, y in dots]
    width = max(xs) - min(xs)
    height = max(ys) - min(ys)
    return width * height