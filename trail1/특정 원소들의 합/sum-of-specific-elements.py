n = 4
arr_2d = []
for _ in range(n):
    arr_1d = list(map(int, input().split()))
    arr_2d.append(arr_1d)

sum = 0
for i in range(n):
    for j in range(n):
        if j >= i:
            sum += arr_2d[j][i]

print(sum)
