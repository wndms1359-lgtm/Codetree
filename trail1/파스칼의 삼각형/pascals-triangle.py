N = int(input())

arr = []
for i in range(N):
    matrix = []
    for j in range(i+1):
        matrix.append(1)
    arr.append(matrix)

for i in range(2,N):
    for j in range(1,i):
        arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

for i in range(N):
    for j in range(i+1):
        print(arr[i][j], end= ' ')
    print()