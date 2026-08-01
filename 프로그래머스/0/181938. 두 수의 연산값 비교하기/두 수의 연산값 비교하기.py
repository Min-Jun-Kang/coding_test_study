def solution(a, b):
    answer = 0
    plus = str(a)+str(b)
    multi = 2*a*b
    if int(plus) >= multi:
        answer = int(plus)
    else:
        answer = multi
    return answer