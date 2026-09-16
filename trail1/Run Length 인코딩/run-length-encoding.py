A = input()
count = 1
answer = ""

if len(A) == 1 :
    answer = answer + A[0] + "1"
else:
    for i in range(1,len(A)-1):
        if  A[i] == A[i-1]:
            count += 1
        else:
            answer = answer + A[i-1] + str(count)
            count = 1
    
    if A[-1] == A[-2]:
        count += 1
        answer = answer + A[-1] + str(count)
    else:
        answer = answer + A[-2] + str(count)
        answer = answer + A[-1] + "1"

answer_length = 0
for i in answer:
    answer_length += 1





print(answer_length)    
print(answer)
