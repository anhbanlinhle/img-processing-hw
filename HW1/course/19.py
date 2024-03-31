n = int(input())

students = []

for i in range(n):
    name = input()
    score = float(input())
    students.append((score, name))

students.sort()
second_score = [score for score, name in students if score != students[0][0]][0]
second_students = sorted(name for score, name in students if score == second_score)

for name in second_students:
    print(name)