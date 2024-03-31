dict = {}

n = int(input())
for i in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    dict[name] = scores

name = input()
print("{:.2f}".format(sum(dict[name]) / len(dict[name])))