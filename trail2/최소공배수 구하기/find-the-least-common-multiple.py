n, m = map(int, input().split())

# Please write your code here.
answer = 0

for i in range(1, n*m+1):
    if (i % n == 0) and (i % m == 0):
        answer = i
        break

print(answer)