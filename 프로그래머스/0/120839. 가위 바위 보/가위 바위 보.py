def solution(rsp):
    win = {'2': '0', '0': '5', '5': '2'}
    return ''.join(win[c] for c in rsp)
