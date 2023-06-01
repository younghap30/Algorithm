import sys
sys.setrecursionlimit(10000)

N, M = map(int, input().split())
arrive = False
A = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)


def dfs(now, depth):
    global arrive
    if depth == 5:  # 깊이가 5가 되면 종료
        arrive = True
        return
    visited[now] = True
    for i in A[now]:
        if not visited[i]:
            dfs(i, depth + 1)  # 재귀 호출마다 깊이 증가
    visited[now] = False


for _ in range(M):
    s, e = map(int, input().split())
    # 양방향 에지이므로 양쪽에 에지 더하기
    A[s].append(e)
    A[e].append(s)

for i in range(N):
    dfs(i, 1)
    if arrive:
        break

if arrive:
    print(1)
else:
    print(0)
