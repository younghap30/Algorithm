n = int(input())
m = int(input())

g = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)


def dfs(v):
    visited[v] = True
    for i in g[v]:
        if not visited[i]:
            dfs(i)


dfs(1)

answer = 0
for i in visited:
    if i is True:
        answer += 1
print(answer - 1)
