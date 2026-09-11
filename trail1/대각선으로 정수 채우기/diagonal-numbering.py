N, M = map(int, input().split())

arr = []
for i in range(N):
    matrix = []
    for j in range(M):
        matrix.append(0)
    arr.append(matrix)

num =1

#첫번째 행에서 시작하는 대각선
for j in range(M):
    r = 0
    c= j
    while r < N and c >= 0:
        arr[r][c] = num
        num += 1
        r += 1
        c -= 1

#마지막 열에서 시작하는 대각선 
for i in range(1,N):
    r = i 
    c = M-1

    while r < N and c >= 0:
        arr[r][c] = num
        num += 1
        r+=1
        c-=1

for i in range(N):
    for j in range(M):
        print(arr[i][j], end= ' ')
    print()

