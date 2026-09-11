N = int(input())

arr= []
for i in range(N):
    matrix= []
    for j in range(N):
        matrix.append(1)
    arr.append(matrix)

for i in range(1,N):
    for j in range(1,N):
        arr[i][j] = arr[i-1][j] + arr[i-1][j-1]+ arr[i][j-1]

for i in range(N):
    for j in range(N):
        print(arr[i][j], end= ' ')
    print()
    