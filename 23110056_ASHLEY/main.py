n = int(input())

employees = []

for i in range(n):
    record = input().strip()
    name, department, score = record.split(",")
    employees.append((department, float(score), name, record))

employees.sort(key=lambda x: (x[0], -x[1], x[2]))

for emp in employees:
    print(emp[3])
