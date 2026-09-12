TC = ["apple", "banana", "grape", "blueberry", "orange"]
N = input()
cnt=0

for i in TC:
    if (i[2] == N) or (i[3] == N):
        print(i)
        cnt += 1
    else: 
        continue
print(cnt)

'''
주의 ! 
    if ( i[2] or i[3]) == N:

위의 코드가 잘못된 이유

i[2] = 'n'
i[3] = 'a'
N = 'a' 인 경우 

if (n or a) == N: #or 연산자는 빈연산자와 0이 아닌 값들은 모두 true로 취급되므로
('n' or 'a') 는 'a'를 볼 필요없이 'n'으로 됨. 
따라서 위의 작성된 코드의 조건은  if 'n' == 'N':이 되어 잘못된 코드가 됨.
'''

