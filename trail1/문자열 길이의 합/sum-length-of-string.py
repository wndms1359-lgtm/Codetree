N = int(input())
arr= []
for i in range(N):
    row = input()
    arr.append(row)

cnt = 0
length = 0
for i in range(len(arr)):
    if arr[i][0] == 'a':
        cnt += 1
    for j in arr[i]:
        length +=1

print(length, cnt)
        
