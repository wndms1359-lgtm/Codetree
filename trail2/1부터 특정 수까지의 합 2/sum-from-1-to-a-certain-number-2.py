N = int(input())

# Please write your code here.
def plus(N):
    if N == 1 :
        return 1
    
    return N + plus(N-1)

print(plus(N))