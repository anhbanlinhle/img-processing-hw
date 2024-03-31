from collections import OrderedDict

n = int(input())

products = OrderedDict()

for i in range(n):
    line = input().split()
    name = ' '.join(line[:-1])
    price = int(line[-1])
    if name in products:
        products[name] += price
    else:
        products[name] = price

for name, price in products.items():
    print(name, price)