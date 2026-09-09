score = list(map(int, input().split()))
new_score = []
count_score = [0] * 11
for i in score:
    if i == 0 :
        break
    else:
        new_score.append(i//10)

for i in new_score:
    count_score[i] +=1

for i in range(10,0,-1):
    print(f'{i}0 - {count_score[i]}')

