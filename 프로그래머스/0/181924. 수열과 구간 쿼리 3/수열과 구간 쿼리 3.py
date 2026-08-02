def solution(arr, queries):
    answer = []
    for idx, [i,j] in enumerate(queries):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
    answer = arr
    return answer