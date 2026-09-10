arr = []

for i in range(2):
    row = list(map(int, input().split()))
    arr.append(row)

for i in range(2):
    sum = 0
    for j in range(4):
        sum += arr[i][j]        
    avg = round(sum / 4, 1)
    print(avg, end= ' ')
print()

for j in range(4):
    sum = 0
    for i in range(2):
        sum += arr[i][j]
    avg = round (sum /2, 1)
    print(avg, end= ' ')
print()

sum = 0
for i in range(2):
    for j in range(4):
        sum += arr[i][j]
avg = round(sum/8 , 1)
print(avg)
