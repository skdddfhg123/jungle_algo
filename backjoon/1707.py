import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def dfs(V, flag):
	global ans
	if ans == "NO":
		return
	vis[V] = flag
	for i in graph[V]:
		if not vis[i]:
			dfs(i, -flag)
		elif vis[V]==vis[i]:
			ans = "NO"
			return

K = int(input())
for _ in range(K):
	N, E = map(int,input().split())
	graph = [[] for _ in range(N + 1)]
	vis = [0] * (N + 1)
	for _ in range(E):
		a, b = map(int, input().split())
		graph[a].append(b)
		graph[b].append(a)
	ans = "YES"
	for i in range(1, N + 1):
		if vis[i] == 0:
			dfs(i, 1)
			if ans == "NO":
				break

	print(ans)
