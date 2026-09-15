S, Q = list(input().split())
S = list(S)
Q = int(Q)

for i in range(Q):
    question = list(input().split())
    if question[0] == '1':
        a = int(question[1])
        b= int(question[2])
        S[a-1], S[b-1] = S[b-1], S[a-1]
        for i in range(len(S)):
            print(S[i], end='')
        print()
    if question[0] == '2':
        for i in range(len(S)):
            if S[i] == question[1]:
                S[i] = question[2]
        for i in range(len(S)):
            print(S[i], end='')
        print()

