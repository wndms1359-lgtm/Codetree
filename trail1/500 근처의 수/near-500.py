tc = list(map(int,input().split()))
max_value = -999999999999999999999
min_value = 9999999999999999999999

for i in tc:
    if (i > max_value) and (i < 500):
        max_value = i
    if (i > 500) and (i < min_value):
        min_value = i

print(max_value, min_value)
    
