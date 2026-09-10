N = int(input())
tc = list(map(int,input().split()))

min = 9999999999

for i in range(1,N):
    if min > (tc[i]- tc[i-1]) :
        min = (tc[i]- tc[i-1])

print(min)