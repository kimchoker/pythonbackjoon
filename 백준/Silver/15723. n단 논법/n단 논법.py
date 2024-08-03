import sys
from collections import defaultdict


def add_point(name):
    if name not in relations:
        relations[name] = set()


def add_edge(fromm, to):
    if fromm in relations:
        relations[fromm].add(to)


def dfs(fromm, to, visited):
    # 목적지에 도달했으면 True
    if fromm == to:
        return True

    # 이미 방문한 노드라면 False
    if fromm in visited:
        return False

    visited.add(fromm)

    # 현재 노드의 모든 이웃 노드에 대해 DFS 탐색
    for neighbor in relations.get(fromm):
        if dfs(neighbor, to, visited):
            return True

    return False


def is_this_in_there(fromm, to):
    visited = set()
    if dfs(fromm, to, visited):
        return 'T'
    else:
        return 'F'


relations = defaultdict(set)
# 전제 수
proposition = int(sys.stdin.readline().strip())

for _ in range(proposition):
    fromm, to = sys.stdin.readline().strip().split(" is ")
    add_point(fromm)
    add_point(to)
    add_edge(fromm, to)

inference = int(sys.stdin.readline().strip())

for _ in range(inference):
    fromm, to = sys.stdin.readline().strip().split(" is ")
    print(is_this_in_there(fromm, to))
