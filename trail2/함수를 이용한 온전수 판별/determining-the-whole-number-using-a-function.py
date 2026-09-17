a, b = map(int, input().split())

# Please write your code here.

def f(a,b):
    arr= []
    for i in range(a,b+1):
        if (i % 2 == 0) or (i%10 == 5) or ( i%3 ==0 and i%9 != 0):
            continue
        else:
            arr.append(i)

    count = 0
    for i in arr:
        count += 1
    
    return count

print(f(a,b))
        
#연산자 우선순위에서 or이 마지막 