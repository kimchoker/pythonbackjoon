count = int(input())

origin = []
sliced = []
result = []

for _ in range(count):
    origin.append(input().split())

for sublist in origin:
    current_list = []
    
    for item in sublist:

        if item.isdigit():
            current_list.append(item)

        else:
            current_list.extend(list(item))

    sliced.append(current_list)

for each in sliced:
    word = ''
    count = int(each[0])
    result.append(''.join([char * count for char in each[1:]]))

for answer in result:
    print(answer)
    