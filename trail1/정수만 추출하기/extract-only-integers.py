A, B = input().split()

arr1 = '' 
arr2 = ''
for i in A:
    if i.isdigit() == True:
        arr1 += i
    else:
        break

for i in B:
    if i.isdigit() == True:
        arr2 += i
    else:
        break
print(int(arr1) + int(arr2))


         