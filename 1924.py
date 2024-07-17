m, d = map(int, input().split())

# 각 달의 날짜를 배열로 만듬
year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 요일을 배열로 만듬
day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

# 입력된 날짜를 365일 중 몇번째 날인지로 변환
date = 0

for i in range(m - 1):
    date = date + year[i]

date += d

# 입력된 날짜의 요일을 계산
chosen = date % 7

# 출력
print(day[chosen])