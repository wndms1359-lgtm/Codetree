TC = list(input()) #input()함수의 결과는 str객체로 만들어짐. 인덱스로 값 변경은 str객체의 경우 불가능하기에 list로 바꿔줌.

a = TC[0]
b = TC[1] 

for i in range(len(TC)):
    if TC[i] == a:
        TC[i] = b
        continue
    if TC[i] == b:
        TC[i] = a

for i in range(len(TC)):
    print(TC[i], end='')

