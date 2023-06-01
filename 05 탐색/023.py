import sys

sys.setrecursionlimit(10000)
n, m = map(int, input().split())
A = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)


def dfs(v):
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            dfs(i)


for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    # 양방향 에지이므로 양쪽에 에지를 더하기
    A[s].append(e)
    A[e].append(s)

count = 0

for i in range(1, n + 1):
    if not visited[i]:
        count += 1
        dfs(i)

print(count)
