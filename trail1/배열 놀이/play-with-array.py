N = list(map(int, input().split()))

tc = list(map(int, input().split())) # K개의 원소 리스트 

Q = []
for i in range(N[-1]):
    Q.append(list(map(int, input().split())))
    
for i in Q:
    if i[0] ==  1:
        r = i[-1]
        print(tc[r-1])
    if i[0] == 2:
        idx = -1
        for k in range(len(tc)):
            if tc[k] == i[-1]:
                idx = k
                print(k+1)
                break
        if idx == -1:
            print(0)
    if i[0] == 3:
        for t in range(i[1], i[2]+1):
            print(tc[t-1] , end = ' ')
        print()

