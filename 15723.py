# 접근
# a는 b가 될 수 있음 그러나 반대로 b는 a가 될 수 없음 a는 b의 요소일 뿐
# 그래서 b 가 c 라면 a도 c가 될 수 있음
# 인접 리스트를 이용해 노드를 추가하고, 간선을 만들어준다.
# 간선을 만들 때, from 에 a에 들어있는 요소가 들어온 경우 to에 들어온 값을 a에도 추가

import sys


def add_point(name):
    if name not in relations:
        relations[name] = []


def add_edge(fromm, to):
    if fromm not in relations or to not in relations:
        return

        # fromm 에 to를 추가
    if to not in relations[fromm]:
        relations[fromm].append(to)

        # fromm 이 다른 노드에 연결되어 있는 경우, 그 노드에 to를 추가
    for i in relations:
        if fromm in relations[i] and to not in relations[i]:
            relations[i].append(to)


def is_this_in_there(fromm, to):
    if to in relations[fromm]:
        return 'T'
    else:
        return 'F'


relations = {}
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