n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
def f():
    global m
    arr = [A[m-1],]
    while m != 1:
        if m % 2 == 0:
            m = m//2
            arr.append(A[m-1])
        else:
            m -= 1
            arr.append(A[m-1])
    
    print(sum(arr))

f() 

        


