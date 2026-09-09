N = list(map(int,input().split()))
A = list(map(int,input().split()))
B = list(map(int,input().split()))
cnt= -1
for i in range(N[0] -N[1]+1):
    if A[i:i+N[1]] == B:
        cnt=0
        print("Yes")
if cnt == -1:
    print("No")
