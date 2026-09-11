TC = list(input().split())

arr= []
for i in range(2):
    arr.append(len(TC[i]))
if arr[0] == arr[1]:
    print("same")
elif arr[0] > arr[1]:
    print(TC[0], arr[0])
else: 
    print(TC[1], arr[1])