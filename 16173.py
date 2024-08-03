import sys


def add_point(name):
    if name not in relations:
        relations[name] = []


def add_edge(fromm, to):
    if fromm not in relations or to not in relations:
        return


size = int(sys.stdin.readline())
visited = [[False] * size for _ in range(size)]
board = [list(sys.stdin.readline().strip()) for _ in range(size)]


def dfs(board, visited, y, x, size):
    visited[y][x] = True
    if board[y][x] < size:
        # 조건을 오른쪽으로 갔을 때의 수치가 size를 오버하면 다시 아래로도 시도해 보는 식으로 구성해야 할 듯?

