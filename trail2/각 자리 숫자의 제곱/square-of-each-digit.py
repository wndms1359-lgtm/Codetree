N = int(input())

# Please write your code here.

def f(N):
    if N == 0 :
        return 0 

    return (N%10)**2 + f(N//10)


print(f(N))