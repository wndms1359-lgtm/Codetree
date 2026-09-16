A = input()
count = 1
answer = ""

for i in range(1,len(A)):
    if  A[i] == A[i-1]:
        count += 1
    else:
        answer = answer + A[i-1] + str(count)
        count = 1
    
answer = answer + A[-1] + str(count)

answer_length = 0
for i in answer:
    answer_length += 1

print(answer_length)    
print(answer)
