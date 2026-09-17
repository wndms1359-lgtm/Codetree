a, b = map(int, input().split())

# Please write your code here.
def f(a,b):
    arr = []
    for i in range(a,b+1):
        for j in range(2,i):
            if i % j == 0 :
                break
        else:
            arr.append(i)

    return sum(arr)

print(f(a,b))





    
    

    



        