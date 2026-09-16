A = input()
TC = input()

for i in TC:
    if i == 'L':
        A = A[1:] + A[0]
    if i == 'R':
        A = A[-1] + A[0:-1]
print(A)