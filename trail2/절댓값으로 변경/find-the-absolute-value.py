n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def f(n, arr):
    for i in range(n):
        if arr[i] < 0:
            arr[i]= abs(arr[i])
    
    for i in range(n):
        print(arr[i], end=' ')

f(n,arr)