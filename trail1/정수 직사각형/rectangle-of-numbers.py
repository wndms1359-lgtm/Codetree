TC = list(map(int, input().split()))
N = TC[0] #세로변의 길이
M = TC[1] #가로변의 길이

c= 1
for i in range(N):
    for j in range(M):
        print(c, end = " " )
        c+=1
    print()


        
