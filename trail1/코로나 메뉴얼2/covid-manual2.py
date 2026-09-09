tc1 = input().split()
tc2 = input().split()
tc3 = input().split()
result= [0]*5
for i in tc1, tc2, tc3:
    if i[0] == 'Y':
        if int(i[1]) >= 37:
            result[1] +=1
        else: 
            result[3] +=1
    else: 
        if int(i[1]) >= 37:
            result[2] += 1
        else:
            result[4] += 1

for i in range(1,5):
    print(result[i], end = ' ')
if result[1] >= 2:
    print('E')



  


    


