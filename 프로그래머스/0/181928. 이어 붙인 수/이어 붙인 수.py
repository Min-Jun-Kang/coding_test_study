def solution(num_list):
    answer = 0
    odd = ""
    even = ""
    for idx in range(len(num_list)):
        if num_list[idx] % 2 == 1:
            odd += str(num_list[idx])
        else:
            even += str(num_list[idx])
    answer = int(odd) + int(even)
    return answer