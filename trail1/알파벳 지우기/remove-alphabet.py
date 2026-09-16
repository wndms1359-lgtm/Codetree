A = input()
B = input()

arr1 = ""
arr2 = ""

for i in A:
    if i.isdigit() == True:
        arr1 += i

for i in B:
    if i.isdigit() == True:
        arr2 += i

arr1 = int(arr1)
arr2 = int(arr2)

print(arr1 + arr2)
