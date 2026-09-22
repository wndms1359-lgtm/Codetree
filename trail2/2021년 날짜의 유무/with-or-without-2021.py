M, D = map(int, input().split())

# Please write your code here.


def f(M,D):
    if M <= 7:
        if M % 2 == 1:
            if D <= 31:
                return True
            
    elif M == 2:
        if D<= 28:
            return True
        else:
            if D <= 30:
                return True #홀수이면 31 2이면 28 다른 짝수는 30이면 참
    elif M <= 12:
        if M % 2 ==0:
            if D <= 31:
                return True
        else:
            if D <= 30:
                return True
    else:
        return False

if f(M,D):
    print("Yes")
else:
    print("No")



# 1 31
# 2 28
# 3 31
# 4 30
# 5 31
# 6 30
# 7 31


# 8 31
# 9 30
# 10 31
# 11 30
# 12 31

