s = list(input())

# N번째를 제거
while len(s) != 1:
    idx = int(input())
    if idx >= len(s):
        s = s[:-1]
        for i in range(len(s)):
            print(s[i], end='')
        print()
    else:
        s = s[:idx] + s[idx+1:]
        for i in range(len(s)):
            print(s[i], end='')
        print()





