n, m = map(int, input().split())
arr = list(map(int, input().split()))

q = []
for _ in range(m):
    a1, a2 = map(int, input().split())
    q.append((a1, a2))

for i in range(m):
    sum = 0
    for j in range(q[i][0]-1, q[i][1]):
        sum += arr[j] 
    print(sum)
