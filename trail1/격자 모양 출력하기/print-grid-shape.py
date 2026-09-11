N, M = map(int, input().split())

arr= []
for i in range(N):
    matrix= []
    for j in range(N):
        matrix.append(0)
    arr.append(matrix)

for __ in range(M):
    r, c = map(int, input().split())
    arr[r-1][c-1] += 1
    arr[r-1][c-1] *= (r * c)

for i in range(N):
    for j in range(N):
        print(arr[i][j], end= ' ')
    print() 
