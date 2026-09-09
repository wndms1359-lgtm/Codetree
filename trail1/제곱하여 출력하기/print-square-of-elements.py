N = int(input())
tc = list(map(int,input().split()))

for i in range(len(tc)):
    tc[i] = tc[i]**2
    print(tc[i], end =' ')