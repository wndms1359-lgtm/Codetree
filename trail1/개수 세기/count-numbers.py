N = list(map(int,input().split()))

tc = list(map(int, input().split()))

R = N[0] #주어진 숫자 개수 
M = N[1] #찾아야 하는 숫자 
cnt = 0

for i in range(R):
    if tc[i] == M:
        cnt += 1

print(cnt)