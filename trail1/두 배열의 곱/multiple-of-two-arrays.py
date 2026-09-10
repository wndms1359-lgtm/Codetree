arr = []
for i in range(2):
    matrix = []
    for j in range(3):
        row = list(map(int, input().split()))
        matrix.append(row)
    arr.append(matrix)
    if i == 0:
        input()

a = arr[0]
b = arr[1]

for i in range(3):
    for j in range(3):
        print(a[i][j] * b[i][j], end = " ")
    print()



