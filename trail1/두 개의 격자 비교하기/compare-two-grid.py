N, M = map(int, input().split())

arr1 = []
for i in range(N):
    row = list(map(int, input().split()))
    arr1.append(row)

arr2 = []
for i in range(N):
    row = list(map(int, input().split()))
    arr2.append(row)


for i in range(N):
    for j in range(M):
        if arr1[i][j] == arr2[i][j]:
            print(0, end = ' ')
        else:
            print(1, end = ' ')
    print()
    

