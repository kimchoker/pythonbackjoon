# extend() 사용 append() 와 달리 요소 자체를 추가하는것이 아니라 요소의 갯수를 늘려서 넣어줌
# .isdigit() 으로 숫자임을 확인하기

count = int(input())

origin = []
sliced = []
result = []

# 주어진 입력 횟수만큼 입력을 받아 origin 리스트에 추가
for _ in range(count):
    origin.append(input().split())

# origin 리스트 안의 각 서브 리스트를 순회
for sublist in origin:
    current_list = []

    for item in sublist:
        # 숫자인 경우 current_list 에 그대로 추가
        if item.isdigit():
            current_list.append(item)
        # 문자인 경우 각 문자를 개별 요소로 current_list 에 추가
        else:
            current_list.extend(list(item))
    # current_list 를 result 에 추가
    sliced.append(current_list)

for each in sliced:
    word = ''
    count = int(each[0])
    result.append(''.join([char * count for char in each[1:]]))

for answer in result:
    print(answer)
