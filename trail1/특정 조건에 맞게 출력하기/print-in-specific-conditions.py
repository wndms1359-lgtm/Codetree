tc = list(map(int,input().split()))

for i in range(len(tc)):
    if tc[i] == 0:
        break
    
    else: 
        if tc[i] % 2 == 1:
            print(tc[i]+3 , end= ' ')
        else:
            print(tc[i]//2, end= ' ')

