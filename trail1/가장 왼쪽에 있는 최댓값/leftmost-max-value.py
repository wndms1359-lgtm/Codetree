n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
arr = []
idx_max = -1
while idx_max != 0:
    max = a[0]
    idx_max = 0
    for i in range(n):
        if a[i] > max:
            idx_max = i
            max = a[i]
    arr.append(idx_max +1)
    n = idx_max

print(*arr)
