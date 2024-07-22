case = int(input())

data = []
above = []
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




