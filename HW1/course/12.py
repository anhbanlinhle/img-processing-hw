from collections import defaultdict
n, m = map(int, input().split())
d = defaultdict(list)

for i in range(n):
    string = input()
    d[string].append(i + 1)

for i in range(m):
    string = input()
    if string in d:
        print(" ".join(map(str, d[string])))
    else:
        print(-1)
