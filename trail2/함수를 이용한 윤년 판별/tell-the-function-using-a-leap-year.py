y = int(input())

# Please write your code here.

def f(y):
    if (y % 4 != 0) or (y % 100 == 0 and y% 400 != 0):
        return "false"
    else:
        return "true"
print(f(y))  