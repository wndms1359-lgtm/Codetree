N = int(input())
tc = list(map(int, input().split()))
cnt = 0
for i in range(N):
    if tc[i] == 2 :
        cnt += 1
    if cnt == 3:
        print(i+1)
        break
