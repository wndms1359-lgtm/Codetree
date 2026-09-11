N, M = map(int, input().split())


    
arr = []
for i in range(N):
    row= []
    for j in range(N):
        row.append(0)
    arr.append(row)
    
cnt = 1    
for __ in range(M):
    r,c = map(int, input().split())
    arr[r-1][c-1] += cnt
    cnt += 1

for i in range(N):
    for j in range(N):
        print(arr[i][j], end=' ')
    print()
