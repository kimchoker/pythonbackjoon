column, row = map(int, input().split())
list = []
for i in range(column):
    list.append(input()[::-1])


for i in range(column):
    print(list[i])