N = int(input())

arr = input().split()

length = 0
result = ""

for i in arr:
    result += i

for i in range(0,len(result),5):
    print(result[i:i+5])




