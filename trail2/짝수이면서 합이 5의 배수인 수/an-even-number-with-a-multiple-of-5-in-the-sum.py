n = int(input())

# Please write your code here.

def f(n):
    if n % 2 == 0 :
        n = str(n)
        sum = 0
        for i in n:
            sum += int(i)
        if sum % 5 == 0:
            return "Yes"
        else:
            return "No"
    else:
        return "No"

print(f(n)) 
            
