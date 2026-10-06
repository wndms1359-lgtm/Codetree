n = int(input())

# Please write your code here.

def count(n):
    if n == 0:
        return
    count(n-1)
    print(n, end=' ')


def count_reverse(n):
    if n == 0:
        return
    print(n, end= ' ')
    count_reverse(n-1)

count(n)
print()
count_reverse(n)