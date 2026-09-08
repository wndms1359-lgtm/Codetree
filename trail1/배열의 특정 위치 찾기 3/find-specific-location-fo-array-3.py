tc = list(map(int, input().split()))
result = 0

for i in range(len(tc)):
    if tc[i] == 0:
        result = tc[i-1] + tc[i-2] + tc[i-3]
        break
    
print(result)