tc = list(map(int, input().split()))
N = len(tc)
result_1 = 0
result_2 = 0
for i in range(N): 
    if i % 2 == 0: #첫번째, 세번째 등 홀수번째 값들은 인덱스 번호가 0번, 2번 즉 짝수번째임. 
        result_1 += tc[i] 
    else:
        result_2 += tc[i]



print(abs(result_1 - result_2))