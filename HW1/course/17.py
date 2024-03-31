from collections import namedtuple

n, Student = int(input()), namedtuple('Student', input().split())
avg = sum([int(Student(*input().split()).MARKS) for i in range(n)]) / n
print("{:.2f}".format(avg))
