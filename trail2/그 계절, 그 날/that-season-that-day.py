Y, M, D = map(int, input().split())

# Please write your code here.

def check(Y,M,D):
    a = M % 12 
    if a <= 2:
        if M ==2:
            if (Y % 4 == 0 and Y % 100 != 0) or (Y % 400 == 0):
                if D <= 29:
                    return "Winter"

            else:
                if D<= 28:
                    return "Winter"
        else:
            if D <= 31:
                return "Winter"

    elif a<=5 :
        if (M % 2)!= 0:
            if D <= 31:
                return "Spring"
        else:
            if D <= 30:
                return "Spring"

    elif a<= 8:
        if M % 6 == 0:
            if D <= 30:
                return "Summer"
        else:
            if D<= 31:
                return "Summer"

    elif a<= 11:
        if M % 10==0:
            if D <= 31:
                return "Fall"
        else:
            if D<= 30:
                return "Fall"
    return -1    
    

a = check(Y,M,D)
print(a)