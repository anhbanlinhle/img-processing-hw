from collections import Counter

X = int(input())
shoes = list(map(int, input().split()))
shoes = Counter(shoes)

sum = 0

Y = int(input())
for i in range(Y):
    shoe, price = map(int, input().split())
    if shoes[shoe] > 0:
        sum += price
        shoes[shoe] -= 1

print(sum)
