arr = []
for _ in range(3):
    arr.append(input())

result= []
for i in arr:
    result.append(len(i))

print(max(result)- min(result))
