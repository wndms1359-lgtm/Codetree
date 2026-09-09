N = int(input())
tc = list(map(int, input().split()))

for i in range(len(tc)):
    if tc[i] % 2 == 0:
        print(tc[i], end = ' ')