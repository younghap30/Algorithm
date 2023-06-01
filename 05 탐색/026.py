from collections import deque

n, m, start = map(int, input().split())
A = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e = map(int, input().split())
    # 양방향 에지이므로 양쪽에 에지를 더하기
    A[s].append(e)
    A[e].append(s)

for i in range(n + 1):
    A[i].sort()  # 번호가 작은 노드부터 방문하기 위해 정렬하기


def dfs(v):
    print(v, end=' ')
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            dfs(i)


visited = [False] * (n + 1)
dfs(start)


def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now_node = queue.popleft()
        print(now_node, end=' ')
        for i in A[now_node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


print()
visited = [False] * (n + 1)  # 리스트 초기화
bfs(start)
