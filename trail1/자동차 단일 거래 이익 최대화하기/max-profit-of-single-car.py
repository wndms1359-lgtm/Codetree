N = int(input())
price = list(map(int, input().split()))

# Please write your code here.
min_price = price[0]
max_profit = 0

for i in range(1,N):
    profit = price[i] - min_price
    if profit > max_profit:
        max_profit = profit
    if price[i] < min_price:
        min_price = price[i]

print(max_profit)

