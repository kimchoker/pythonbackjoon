origin = input()
count = 0

while len(origin) > 1:
    count += 1
    answer = 0
    for i in origin:
        answer += int(i)
        origin = str(answer)

print(count)

if int(origin) % 3 == 0:
    print('YES')
else:
    print('NO')

