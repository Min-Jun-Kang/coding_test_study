def solution(num_list):
    answer = 0
    mul_total = 1
    sum_total = 0
    for idx in range(len(num_list)):
        mul_total *= num_list[idx]
        sum_total += num_list[idx]
    if mul_total < sum_total**2:
        answer = 1
    return answer