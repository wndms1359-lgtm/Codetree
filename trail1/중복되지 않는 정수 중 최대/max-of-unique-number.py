n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
idx = -1
cnt = [0] * 1001
for t in nums:
    cnt[t] += 1

result= []
for i in range(1001):
    if cnt[i] == 1:
        idx = i
        result.append(i)

if idx == -1:
    print(idx)

else:
    max_value = result[0]
    for x in result:
        if x > max_value:
            max_value = x
    print(max_value)
