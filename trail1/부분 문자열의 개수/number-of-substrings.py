A = input()
B = input()

a = len(A)
b = len(B)

count = 0
for i in range(a-b+1):
    if A[i:i+b] == B:
        count+=1

print(count)

