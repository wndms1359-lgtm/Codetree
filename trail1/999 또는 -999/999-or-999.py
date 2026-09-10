N = list(map(int, input().split()))
T = len(N)
idx = 0
for i in range(T):
    if N[i] == (999 | -999):
        idx = i 

result = N[0:i]
max_v = N[0]
min_v = N[0]

for x in result:
    if x > max_v:
        max_v = x
    if x < min_v:
        min_v = x
    
print(max_v, min_v) 
