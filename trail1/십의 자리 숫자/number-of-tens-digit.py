tc = list(map(int,input().split()))
count_arr = [0] * 100
for i in tc:
    if i == 0 :
        break
    else :
        count_arr [i // 10] += 1 
        

for i in range(1,10):
    cnt = count_arr[i]
    print(f'{i} - {count_arr[i]}')