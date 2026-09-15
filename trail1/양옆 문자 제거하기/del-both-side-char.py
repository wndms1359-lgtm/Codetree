S = input() #input()은 기본적으로 문자열(str) 반환 

S = S[0]+ S[2:-2] + S[-1] # 리스트 + 문자열의 경우, 오류 발생 

print(S)
