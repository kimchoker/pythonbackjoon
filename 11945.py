# 첫줄에 들어오는 행과 열을 받음
column, row = map(int, input().split())

# 들어오는 데이터값을 받을 리스트 생성
list = []

# input 값을 슬라이싱 구문을 이용해서 역순으로 list에 저장
for i in range(column):
    list.append(input()[::-1])

# 저장한 값을 출력
for i in range(column):
    print(list[i])