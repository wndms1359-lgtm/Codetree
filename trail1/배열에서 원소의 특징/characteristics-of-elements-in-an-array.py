tc = list(map(int, input().split()))
N = len(tc)
for i in range (N):
    if tc[i] % 3 == 0:
        print(tc[i-1])
        break
    