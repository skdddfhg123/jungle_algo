import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000**3)
N = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
	a, b = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)
vis = set()
ans = [0] * (N + 1)
def dfs(V):
	vis.add(V)
	for i in graph[V]:
		if i not in vis:
			ans[i] = V
			dfs(i)
dfs(1)
for i in range(2, N + 1):
	print(ans[i])
