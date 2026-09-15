N = list(input())

f = N[1]

for i in range(len(N)):
    if N[i] == f:
        N[i] = N[0]

for i in range(len(N)):
    print(N[i], end='')