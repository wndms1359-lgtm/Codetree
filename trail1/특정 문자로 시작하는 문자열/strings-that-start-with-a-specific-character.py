N = int(input())

arr = []
for i in range(N):
    row = input()
    arr.append(row)

TC= input()
length = 0
count = 0
for i in range(N):
    if arr[i][0] == TC:
        count += 1
        length += len(arr[i])

print(f'{count} {length/count:.2f}')