N, M = map(int, input().split())

cnt = 1


for i in range(N):
    for j in range(M):
        print(cnt, end= ' ')
        cnt += 1
    print()
