def solution(l, r):
    answer = []
    for i in range(l, r+1):
        flag = True
        for j in str(i):
            if j != "0" and j != "5":
                flag = False
                break
        if flag:
            answer.append(i)
    if len(answer) == 0:
        answer.append(-1)
    return answer