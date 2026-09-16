A = input()
B = input()

size = len(B)
# Please write your code here.

while True:
    if A.find(B) == -1:
        print(A)
        break
    else:
        idx = A.find(B)
        A = A[0:idx] + A[idx+size:]