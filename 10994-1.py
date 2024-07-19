number = int(input())

# 별과 공백의 상수 선언
STAR = '*'
BLANK = ' '

# input 숫자에 따른 규칙
rule = 4 * number - 3

# 네모를 줄마다 저장해 줄 배열을 생성 각 요소는 공백으로
square = [[BLANK] * rule for _ in range(rule)]


# 사각형을 그려줄 함수 생성
def drawStars(count, x, y):
    edge_length = 4 * count - 3
    if count == 1:
        square[x][y] = STAR
        return

    for i in range(0, edge_length):
        # 윗줄 가로변
        square[x][y + i] = STAR
        # 아랫줄 가로변
        square[x + (edge_length - 1)][y + i] = STAR
        # 왼쪽 세로변
        square[y + i][x] = STAR
        # 오른쪽 세로변
        square[x + i][y + (edge_length - 1)] = STAR

    # count 값을 줄여 다음 함수의 edge_length 를 줄여주고, (x, y)를 대각선으로 한칸 이동
    count -= 1
    x += 2
    y += 2

    # 줄인 값으로 재실행
    drawStars(count, x, y)


drawStars(number, 0, 0)

for lines in square:
    print(''.join(map(str, lines)))
