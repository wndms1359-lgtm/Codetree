arr= []
for i in range(5):
    matrix = []
    for j in range(5):
        matrix.append(1)
    arr.append(matrix)

cnt= 1

for i in range(1,5):
    for j in range(1,5):
        arr[i][j] = arr[i-1][j] + arr[i][j-1]

for i in range(5):
    for j in range(5):
        print(arr[i][j], end= ' ')
    print()
        