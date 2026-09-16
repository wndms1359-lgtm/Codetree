n , A = input().split()
n = int(n)
cnt = 0
arr = []
for i in range(n):
    row = input()
    arr.append(row)

for i in arr:
    if i == A:
        cnt += 1

print(cnt)