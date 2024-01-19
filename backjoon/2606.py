import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(1000 ** 3)

N = int(input())
M = int(input())

graph = [[False] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
	a, b = map(int, input().split())
	graph[a][b] = True
	graph[b][a] = True
vis = [False] * (N + 1)
def dfs(V):
	vis[V] = True
	for i in range(1, N + 1):
		if not vis[i] and graph[V][i]:
			dfs(i)
ans = 0
dfs(1)
for i in range(1, len(vis)):
	if vis[i]:
		ans+=1
print(ans - 1)