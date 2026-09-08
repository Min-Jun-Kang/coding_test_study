n = 2
arr_2d = []
for i in range(n):
    arr_1d = list(map(int, input().split()))
    arr_2d.append(arr_1d)


# 가로 평균
for i in range(len(arr_2d)):
    sum = 0
    for j in range(len(arr_1d)):
        sum += arr_2d[i][j]
    avg = round(sum / len(arr_1d), 1)
    print(avg, end=" ")
print()
# 세로 평균
for i in range(len(arr_1d)):
    sum = 0
    for j in range(len(arr_2d)):
        sum += arr_2d[j][i]
    avg = round(sum / len(arr_2d), 1)
    print(avg, end=" ")
# 전체 평균
sum = 0
print()
for i in range(len(arr_2d)):
    for j in range(len(arr_1d)):
        sum += arr_2d[i][j]
avg = round(sum / (len(arr_1d) * len(arr_2d)), 1)
print(avg, end=" ")
