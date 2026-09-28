A = input()

# Please write your code here.
X = len(A)
def f(A):
    for i in range(X//2):
        if A[i] != A[-(i+1)]:
            return "No"
    else:
        return "Yes"

print(f(A))





