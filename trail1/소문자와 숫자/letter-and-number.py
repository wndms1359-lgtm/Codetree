N = input()
arr = "" 

for i in N:
    if i.isalpha() == True:
        arr += i.lower()
    elif i.isdigit() == True:
        arr += i
    else:
        continue

print(arr)
