tc = list(map(int, input().split()))

for i in range(2,10):
    tc.append(tc[i-1]+ 2*tc[i-2])


for i in range(10):
    print(tc[i], end= ' ')