import sys

height, width = map(int, sys.stdin.readline().strip().split(' '))

grass = []
count = 0

for i in range(height):
    grass.append(sys.stdin.readline().strip())

for y in range(len(grass)):
    for x in range(len(grass[y])):
        current = grass[y][x]

        if current == '#':
            # 첫째줄 첫번째가 # 인 경우
            if y == 0 and x == 0:
                count += 1
            # 첫째줄 중 # 가 있는 경우
            elif y == 0 and grass[y][x - 1] != '#':
                count += 1
            # 첫째줄 이후 첫번째 값이 # 인 경우
            elif x == 0 and grass[y - 1][x] != '#':
                count += 1
            # 첫째줄 이후 # 가 있는 경우 이전 좌표에 #가 없고 이전 줄에 #가 없으면
            elif grass[y][x - 1] != '#' and grass[y - 1][x] != '#':
                count += 1


print(count)
