# 테스트 케이스를 먼저 입력받음
case = int(input())

# 각 테스트 결과를 받을 배열 먼저 생성
data = []

# 테스트 케이스만큼
for exam in range(case):
    line = input()
    data.append(list(map(float, line.split())))

for i in range(len(data)):
    sumData = sum(data[i]) - data[i][0]
    avg = sumData / data[i][0]
    cnt = 0
    e = 1
    for e in range(1, len(data[i])):
        if data[i][e] > avg:
            cnt += 1

    abvAvg = (cnt / data[i][0]) * 100
    formatted = f"{abvAvg:.3f}%"
    print(formatted)




