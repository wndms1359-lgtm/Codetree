N = int(input())
arr = list(map(int, input().split()))
count_arr = [0] * 10

for i in arr:
    count_arr[i] +=1
for i in range(1,10):
    cnt = count_arr[i]
    print(cnt)

