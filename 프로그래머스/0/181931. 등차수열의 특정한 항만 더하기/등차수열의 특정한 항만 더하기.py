def solution(a, d, included):
    answer = 0
    total = 0
    list = []
    list.append(a)
    for idx in range(1, len(included)):
        list.append(a+d*idx)
    for idx in range(len(included)):
        if included[idx] == True:
            total += list[idx]
    answer = total
    return answer