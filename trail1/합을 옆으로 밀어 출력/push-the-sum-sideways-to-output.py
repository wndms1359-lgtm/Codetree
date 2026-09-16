N = int(input())
arr = []

for i in range(N):
    row = int(input())
    arr.append(row)

tmp = str(sum(arr))

print(tmp[1:]+tmp[0])

