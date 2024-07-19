number = int(input())  # 별 개수

rule = (4 * number) - 3

map_array = [[' '] * rule for _ in range(rule)]

STAR = '*'
BLANK = ' '


def drawStar(n, x, y):
    # 재귀적으로 별 찍기
    global map_array

    edge_length = (4 * n) - 3
    if edge_length == 1:
        map_array[x][y] = STAR
        return

    else:
        for i in range(edge_length):
            map_array[x][y + i] = STAR  # 윗변(1번 선분)
            map_array[y + i][x] = STAR # 좌측변(2번 선분)
            map_array[x + (edge_length - 1)][y + i] = STAR  # 아랫변(3번 선분)
            map_array[x + i][y + (edge_length - 1)] = STAR  # 우측변(4번 선분)
        n = n - 1
        x = x + 2
        y = y + 2

        drawStar(n, x, y)

        return


drawStar(number, 0, 0)

for i in range(rule):
    print(*map_array[i], sep='')
