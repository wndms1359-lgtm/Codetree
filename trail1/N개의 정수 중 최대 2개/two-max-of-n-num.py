n = int(input()) #총 원소 개수 
a = list(map(int, input().split())) #n개의 정수가 공백 사이에 두고 주어짐 

# Please write your code here.

max_arr = []

for _ in range(2):
    max = a[0]
    max_idx = 0
    for i in range(n):
        if a[i] > max:
            max_idx = i
            max = a[i]
    max_arr.append(max)
    a[max_idx] = -9999999999999


print(*max_arr)
