str= input()
count1 = 0
count2 = 0
for i in range(len(str)-1):
    if str[i] + str [i+1] == 'ee':
        count1 += 1
    if str[i] + str [i+1] == 'eb':
        count2 += 1
print(f'{count1} {count2}')