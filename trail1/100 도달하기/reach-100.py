N = int(input())
tc = [ 1, N,] #초기화

for i in range(100):
    if i >= 2:
        tc.append(tc[i-1]+ tc[i-2])
    if tc[-1] > 100:
        break

            
for i in range(len(tc)):
    print( tc[i], end = ' ')

            
