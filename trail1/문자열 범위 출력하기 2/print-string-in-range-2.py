N = input()
tc = int(input())

if len(N) < tc:
    print(N[::-1])
else:
    print(N[-1:-tc-1:-1])




