a, b = map(int, input().split())

# Please write your code here.

def find_num(a, b):
    arr = []
    for i in range(a, b + 1):
        if i == 1:
            arr.append(i)

        else:
            for j in range(2, i-1):
                if i % j == 0:
                    break
            else:
                arr.append(i)
    return arr

def find_sum(arr):
    result = []
    for i in arr:
        sum = 0
        next = i
        while next > 0:
            sum += (next % 10)
            next = next // 10

        result.append(sum)

    return result


def JJack_count(result):
    arr = []
    for i in result:
        if i % 2 == 0:
            arr.append(i)
    
    count= len(arr)
    # print(f'arr : {arr}')
    return count
    # set1 = set(arr)
    # print(f'set : {set1}')

A = find_num(a, b)
# print(A)
B = find_sum(A)
# print(B)
C = JJack_count(B)
print(C)
