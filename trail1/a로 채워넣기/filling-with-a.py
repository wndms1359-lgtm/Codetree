TC = list(input())

TC[1] = 'a'
TC[-2] = 'a'

for i in range(len(TC)):
    print(TC[i],end='')