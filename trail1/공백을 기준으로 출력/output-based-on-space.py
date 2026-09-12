arr1 = input().split() #arr1 = ['Code', 'Tree']
arr2 = input().split() #arr2 = ['Banana', 'is', 'Good']


for i in *arr1,*arr2: 
    print(i, end= '')

'''

*arr1, arr2

# 출력
'Code', 'Tree', ['Banana', 'is', 'Good']

따라서 for가 각각 받는 i는

첫 번째 → 'Code'
두 번째 → 'Tree'
세 번째 → ['Banana', 'is', 'Good']

*arr1 은 리스트의 요소를 하나씩 꺼내라는 뜻
print('내용' , end='')는 print()가 끝날때마다 줄바꿈을 하지만, 이 줄바꿈을 하지않고 바로 뒤에 이어서 쓰겠다는 뜻
'''

