N = input()
idx = -1
answer = list(N)

if 'e' in N:
    idx = N.find('e')
    answer = answer[:idx] + answer[idx+1:]
    for i in range(len(answer)):
        print(answer[i], end='')