import sys

line_count = int(input())

origin_chat = [sys.stdin.readline().strip() for _ in range(line_count)]


count_chat = set()
count_enter = 0
count_imoji = 0

for i in range(len(origin_chat)):
    # ENTER 가 오면 set 을 비움
    if origin_chat[i] == 'ENTER':
        count_chat.clear()
    # count_imoji set에 없으면 요소 추가 후 count_imoji 값을 올려줌
    elif not origin_chat[i] in count_chat:
        count_chat.add(origin_chat[i])
        count_imoji += 1

print(count_imoji)
