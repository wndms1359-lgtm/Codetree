arr= []
for i in range(10):
    row = input()
    arr.append(row)

N = input()

cnt=0
for i in arr:
    if i[-1] == N:
        cnt +=1
        print(i)

if cnt == 0:
    print("None")
     