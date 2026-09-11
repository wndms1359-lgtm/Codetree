N = int(input())

arr = []
for i in range(N):
    matrix = []
    for j in range(N):
        matrix.append(0)
    arr.append(matrix)

    
for i in range(N):
    num= i + 1
    for j in range(N):
        arr[i][j] += num 
        num += N
    

for i in range(N):
    for j in range(N):
        print(arr[i][j], end = ' ')
    print()


