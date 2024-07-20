log_count = int(input())

company = set()

for _ in range(log_count):
    employee = input().split(' ')[0]

    if employee in company:
        company.remove(employee)
    else:
        company.add(employee)

print(" ".join(sorted(company, reverse=True)))
