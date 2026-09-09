N = list(map(int, input().split()))

A = N[0]
B = N[-1]
count_arr = [0] * 10


while A > 1:
    count_arr[A % B] += 1
    A = (A // B)

result= 0 
for i in range(0,10):
    result += (count_arr[i]**2)

print(result)  
