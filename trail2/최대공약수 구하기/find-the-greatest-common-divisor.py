n, m = map(int, input().split())
# Please write your code here.

def find_max_friend(n,m):
    result1 = []
    result2 = []
    for i in range(1,n+1): # 자기 자신도 약수가 되기 때문에 n까지 포함되도록 
        if n % i == 0 :
            result1.append(i)

    for i in result1:
        if m % i == 0 :
            result2.append(i)
    
    return max(result2)

answer = find_max_friend(n,m)
print(answer)


        