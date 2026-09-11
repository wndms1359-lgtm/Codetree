N, M = map(int, input().split())

# Please write your code here.

cnt = 0

arr =[]
for i in range(N):
    matrix = []
    for j in range(M):
        matrix.append(0)
    arr.append(matrix)

for j in range(M):
    if j %2 ==0 :
        for i in range(N):
            arr[i][j] += cnt
            cnt += 1
    else: 
        for i in range(N-1,-1,-1):
            arr[i][j] += cnt
            cnt += 1

for i in range(N):
    for j in range(M):
        print(arr[i][j], end= ' ')
    print()
