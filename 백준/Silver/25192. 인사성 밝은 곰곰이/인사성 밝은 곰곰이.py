import sys

line_count = int(input())

chats = [sys.stdin.readline().strip() for _ in range(line_count)]

count_imoji = set()
count_enter = 0
imoji = 0

for i in range(len(chats)):
    if chats[i] == 'ENTER':
        count_imoji.clear()
    elif not chats[i] in count_imoji:
        count_imoji.add(chats[i])
        imoji += 1

print(imoji)
