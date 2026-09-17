a, b = map(int, input().split())

# Please write your code here.

def f(a,b):
    count = 0
    for i in range(a,b+1):
        x = str(i)
        if any(c in x for c in '369') or ( int(x) % 3 == 0 ):
            count += 1

    return count

print(f(a,b))