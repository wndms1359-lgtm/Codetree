text = input() #입력문자열 길이 N
pattern = input()#목적 문자열 길이M
N = len(text)
M = len(pattern)
# Please write your code here.

def f(a):
    for i in range(a,N):
        if text[a:a+M] == pattern:
            return a

for a in range(N):
    answer = f(a)
    if answer != None:
        print(answer)
        break
else:
    print(-1)

        

