N = int(input())
tc = []
count = 0
for i in range(100):
    tc.append( N * (i+1) ) 
    print(tc[-1], end = ' ')
    if tc[i] % 5 ==0 :
        count += 1
        if count == 2:
            break

