input_str = input()
target_str = input()

input_size = len(input_str)
target_size = len(target_str)
# Please write your code here.

count = 0

for i in range(0 ,(input_size-target_size+1)):
    if input_str[i:i+target_size] == target_str:
        count +=1
        print(i)
        break

if count == 0:
    print(-1)
