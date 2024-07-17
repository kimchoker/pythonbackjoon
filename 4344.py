# 테스트 케이스를 먼저 입력받음
case = int(input())

# 각 테스트 결과를 받을 배열 먼저 생성
data = []

# 테스트 케이스만큼의 줄을 입력받고 줄마다 공백을 기준으로 잘라 배열로 만듬
for exam in range(case):
    line = input()
    data.append(list(map(float, line.split())))

# data배열 길이만큼 for문을 돌리고 그 안의 요소 배열마다 sum 함수를 실행한 뒤 평균값을 구함
for i in range(len(data)):
    sumData = sum(data[i]) - data[i][0]
    avg = sumData / data[i][0]
    cnt = 0
    e = 1
    # 첫번째 data[i]의 첫번째 요소(몇 명인지)를 제외하고 나머지 값을 avg 값과 비교하여 더 클때마다 cnt값을 1씩 올려줌
    for e in range(1, len(data[i])):
        if data[i][e] > avg:
            cnt += 1

    # 계산된 cnt 값을 data[i][0]값(몇 명인지)로 나눠주고 100을 곱해 %로 만들어줌
    abvAvg = (cnt / data[i][0]) * 100

    # f-string을 이용 소숫점 셋째자리까지만 잘라 출력
    formatted = f"{abvAvg:.3f}%"
    print(formatted)




