def solution(arr, queries):
    answer = []
    for idx, [i,j] in enumerate(queries):
        arr[i], arr[j] = arr[j], arr[i]
    answer = arr
    return answer