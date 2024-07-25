origin = input()
count = 0


# 반복적으로 자릿수의 합을 계산
while len(origin) > 1:
    count += 1
    answer = 0
    for i in origin:
        answer += int(i)
        origin = str(answer)

print(count)

# 최종적인 한 자릿수의 결과 확인
if int(origin) % 3 == 0:
    print('YES')
else:
    print('NO')

