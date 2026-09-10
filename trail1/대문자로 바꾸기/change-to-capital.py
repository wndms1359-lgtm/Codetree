arr = []

for i in range(5):
    row = list(input().split())
    arr.append(row)

for i in range(5):
    for j in range(3):
        print(arr[i][j].upper(), end = ' ')
    print()