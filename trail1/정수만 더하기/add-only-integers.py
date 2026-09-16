str = input()
arr = []
answer = 0
for i in str:
    if i.isdigit() == True:
        arr.append(i)



for i in arr:
     answer += int(i)

print(answer)
