#문자 -> 아스키코드값 ord(문자)
#아스키코드값 -> 문자  chr(아스키코드값)

TC = list(map(int, input().split()))

for i in TC:
    print(chr(i), end=' ')