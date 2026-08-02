def solution(code):
    answer = ''
    mode = 0
    for idx in range(len(code)):
        if code[idx] == "1":
            if mode == 0:
                mode = 1
            else:
                mode = 0
        else:
            if mode == 0:
                if idx % 2 == 0:
                    answer += code[idx]
            else:
                if idx % 2 == 1:
                    answer += code[idx]
    if answer == '':
        answer = "EMPTY"
    return answer