n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
min = 999999999999999999999999999999999999999999

for i in a:
    if i < min:
        min = i

count_min = 0

for x in a:
    if x == min:
        count_min += 1

print(min, count_min) 

