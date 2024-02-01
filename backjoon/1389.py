import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))

graph = [[sys.maxsize] * (m + 1) for _ in range(n + 1)]
for i in range(m):
	a, b = list(map(int, input().split()))
	graph[a][b] = 1

for k in range(1, n + 1):
	for i in range(1, n + 1):
		for j in range(1, n + 1):
			graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n + 1):
	for j in range(1, n + 1):
		print(graph[i][j], end=' ')
	print()