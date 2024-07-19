number = int(input())

STAR = '*'
BLANK = ' '

rule = 4 * number - 3

square = [[BLANK] * rule for _ in range(rule)]

def drawStars(count, x, y):
    edge_length = 4 * count - 3
    if count == 1:
        square[x][y] = STAR
        return

    for i in range(0, edge_length):
        square[x][y + i] = STAR
        square[x + (edge_length - 1)][y + i] = STAR
        square[y + i][x] = STAR
        square[x + i][y + (edge_length - 1)] = STAR

    count -= 1
    x += 2
    y += 2

    drawStars(count, x, y)

drawStars(number, 0, 0)

for lines in square:
    print(''.join(map(str, lines)))
