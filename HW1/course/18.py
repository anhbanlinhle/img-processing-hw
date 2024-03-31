a = input()
i, k = input().split()

l = list(a)
l[int(i)] = k
print("".join(l))