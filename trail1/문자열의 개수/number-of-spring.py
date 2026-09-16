N = input()
cnt = 1
arr = []
while N != '0':
    if cnt % 2 == 1:
        arr.append(N)
    cnt += 1
    N = input()

print(cnt-1)
for i in arr:
    print(i)
