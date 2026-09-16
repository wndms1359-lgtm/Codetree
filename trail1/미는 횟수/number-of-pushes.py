A = input()
B = input()
tmp = -1
cnt = 0
for i in range(len(A)):
    if A == B:
        tmp += 1
        break
    else:
        cnt += 1
        A = A[-1] + A[0:-1]

if tmp == -1:
    print(-1)
else:
    print(cnt)

