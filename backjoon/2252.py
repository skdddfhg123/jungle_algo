import sys
from collections import deque
input = sys.stdin.readline

N, M = list(map(int,input().split()))

graph = [[] for _ in range(N + 1)]
check = [0] * (N + 1)
# print(check)

q = deque()
# vis = set()
ans = []
for _ in range(M):
	a, b = list(map(int, input().split()))
	graph[a].append(b)
	check[b] += 1
# print(graph)

for i in range(1, N + 1):
	if check[i] == 0:
		q.append(i)
		# vis.add(i)

while q:
	cur = q.popleft()
	ans.append(cur)
	for i in graph[cur]:
		check[i] -= 1
		if check[i] == 0:
			q.append(i)

print(" ".join(map(str,ans)))
