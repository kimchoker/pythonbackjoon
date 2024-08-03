import sys
from collections import defaultdict, deque


def add_point(name):
    if name not in relations:
        relations[name] = set()


def add_edge(fromm, to):
    if fromm in relations:
        relations[fromm].add(to)


def bfs(start):
    # BFS 탐색을 통해 start 노드에서 도달 가능한 모든 노드를 찾음
    queue = deque([start])
    reachable = set()

    while queue:
        current = queue.popleft()
        if current in reachable:
            continue
        reachable.add(current)

        for neighbor in relations.get(current, []):
            if neighbor not in reachable:
                queue.append(neighbor)

    return reachable


def is_this_in_there(fromm, to):
    reachable_nodes = bfs(fromm)
    return 'T' if to in reachable_nodes else 'F'


# Input processing
relations = defaultdict(set)
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
