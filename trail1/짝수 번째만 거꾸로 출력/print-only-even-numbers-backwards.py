str = input()
result =[]

for i in range(len(str)):
    if i % 2 != 0:
        result.append(str[i])

for i in result[::-1]:
    print(i, end='')