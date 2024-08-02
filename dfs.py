def dfs(graph, v, visited):
    visited[v] = True  # 첫 방문 노드 방문 여부 true
    print(v, end='')  # 현재 방문 노드 출력
    for i in graph[v]:  # 그래프 정보를 순환하면서
        if not visited[i]:  # visited 가 false 이면
            dfs(graph, i, visited)  # 그곳을 방문한다.

    # 그래프 표현법
    graph = [
        [],  # 0번 인덱스는 비워놓고 표현함
        [2, 3, 8],  # 1번 인덱스(node)에 연결 정보, 2, 3, 8과 연결
        [1, 7],  # 2번 연결 정보
        [1, 4, 5],
        [3, 5],
        [3, 4],
        [7],
        [2, 6, 8],
        [1, 7]  # 8번 노드 인접 정보
    ]  # 각 노드가 방문된 정보를 표현하는 1차원 리스트

    visited = [False] * 9  # 1~8번 노드인데 인덱스 0은 사용하지 않기 때문에
    dfs(graph, 1, visited)
