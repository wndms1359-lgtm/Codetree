n = int(input())

# Please write your code here.


def make_rect(n):
    cnt = 1
    for _ in range(n):
        for _ in range(n):
            if cnt > 9:
                cnt = cnt % 9
            print(cnt, end= ' ')
            cnt+= 1
        print() 

make_rect(n)