text = input() #입력문자열 길이 N
pattern = input()#목적 문자열 길이M

# Please write your code here.

def f():
    for i in range(len(text)):
        if text[i:i+len(pattern)] == pattern:
            return i
    return -1
    
print(f()) 
