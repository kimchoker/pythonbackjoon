import sys

coordinates_count = int(sys.stdin.readline().strip())

coordinates = list(map(int, sys.stdin.readline().strip().split(' ')))
origin = [[index, value] for index, value in enumerate(coordinates)]
origin.sort(key=lambda x: x[1])
dictionary = {}
compressed_number = 0

for i in range(len(origin)):
    current = origin[i][1]
    if current not in dictionary:
        dictionary[current] = compressed_number
        origin[i][1] = compressed_number
        compressed_number += 1
    elif current in dictionary:
        origin[i][1] = dictionary[current]

origin.sort(key=lambda x: x[0])

compressed = [str(value) for index, value in origin]

print(' '.join(compressed))