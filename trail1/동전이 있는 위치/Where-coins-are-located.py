N, M = map(int, input().split())

arr= []
for i in range(N):
    matrix= []
    for j in range(N):
        matrix.append(0)
    arr.append(matrix)


for _ in range(M):
    r, c = map(int,input().split())
    arr[r-1][c-1] += 1 

for i in range(N):
    for j in range(N):
        print(arr[i][j], end= ' ')
    print()

'''
핵심

위치 r행 c열 - > 리스트 인덱스 arr[r-1][c-1]에 해당함. 
'''




