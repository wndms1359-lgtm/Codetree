a , b = list(map(int,input().split()))

result = a+b
result = str(result)

count = 0
for i in result:
    if i == '1':
        count += 1

print(count)

