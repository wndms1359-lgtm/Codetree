A = input()

# Please write your code here.
def f(A):
    arr = set()
    for i in A:
        arr.add(i)
    
    if len(arr) >= 2:
        print("Yes")
    else:
        print("No")

f(A)

