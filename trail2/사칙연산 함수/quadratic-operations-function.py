a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.

def f(a,o,c):
    if o not in '+-*/':
        return "False"
    else:
        if o == '+':
            return (f'{a} {o} {c} = {a+c}')
        elif o == '-':
            return (f'{a} {o} {c} = {a-c}')
        elif o == '*':
            return (f'{a} {o} {c} = {a*c}')
        elif o == '/':
            return (f'{a} {o} {c} = {a//c}')

print(f(a,o,c)) 