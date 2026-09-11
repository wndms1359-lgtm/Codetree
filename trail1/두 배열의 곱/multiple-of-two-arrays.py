arr = []
for TC in range(2):
    matrix = []
    for i in range(3):
        row = list(map(int, input().split()))
        matrix.append(row)
    arr.append(matrix)


    if TC == 0:
        input()

X = arr[0]
Y = arr[1]

for i in range(3):
    for j in range(3):
        print(X[i][j] * Y[i][j], end= ' ')
    print()