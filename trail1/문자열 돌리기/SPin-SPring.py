a = input()
L = len(a)

print(a)
for i in range(L):
    a = a[-1]+ a[0:-1]
    print(a)