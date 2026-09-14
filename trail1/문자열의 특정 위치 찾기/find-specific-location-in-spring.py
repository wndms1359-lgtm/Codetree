N = input().split()

arr = N[0]
tc = N[1]

cnt = -1
for i in range(len(arr)):
    if arr[i] == tc:
        cnt += 1
        print(i)
        break

if cnt == -1:
    print("No")