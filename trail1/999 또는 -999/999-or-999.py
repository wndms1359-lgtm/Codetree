tc = list(map(int, input().split()))
max_v = tc[0]
min_v = tc[0]


for i in tc:
    if i == 999 or i == -999:
        break
    if i > max_v:
        max_v = i
    if i < min_v:
        min_v = i

print(max_v, min_v)