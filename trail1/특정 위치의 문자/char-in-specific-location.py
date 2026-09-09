N = [ 'L', 'E' , 'B', 'R', 'O', 'S']

tc = input()

#해당 문자를 찾지 못했다면 -1로 초기화 
idx = -1

#문자탐색 
for i in range(6):
    if N[i] == tc:
        idx = i
        print(i)
        break

if idx == -1:
    print('None')
        

    