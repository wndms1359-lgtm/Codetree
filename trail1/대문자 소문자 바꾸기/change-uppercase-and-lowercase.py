str = input()
answer = ''

for i in str:
    if i >= 'a' and i <= 'z':
        answer += i.upper()
    if i >= 'A' and i <= 'Z':
        answer += i.lower()

print(answer)