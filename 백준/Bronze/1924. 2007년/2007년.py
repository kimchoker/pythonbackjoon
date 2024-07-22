m, d = map(int, input().split())

year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

date = 0

for i in range(m - 1):
    date = date + year[i]

date += d

chosen = date % 7

print(day[chosen])