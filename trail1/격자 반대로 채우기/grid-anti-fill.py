cnt= 1
N= int(input())
arr = []
for i in range(N):
    matrix = []
    for j in range(N):
        matrix.append(0)
    arr.append(matrix)


for j in range(N-1,-1,-1):
    if (N -1 -j) % 2 == 0:
        for i in range(N-1,-1,-1):
            arr[i][j] += cnt
            cnt += 1
    else:
        for i in range(0,N):
            arr[i][j] += cnt
            cnt += 1
            
for i in range(N):
    for j in range(N):
        print(arr[i][j], end= ' ')
    print()
