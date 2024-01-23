import sys
from collections import deque
input = sys.stdin.readline

N, M, K, X = list(map(int,input().split()))

graph = [[] for _ in range(N + 1)]

for _ in range(M):
	a, b = list(map(int,input().split()))
	graph[a].append(b)

q = deque()

q.append([X, 0])
ans = []
vis = set()
vis.add(X)
while q:
	node, dist = q.popleft()
	# print(f"node{node} dist{dist}")
	if dist == K:
		ans.append(node)
	for i in range(len(graph[node])):
		if graph[node][i] not in vis:
			vis.add(graph[node][i])
			q.append([graph[node][i], dist + 1])
ans.sort()

if ans:
	for i in range(len(ans)):
		print(ans[i])
else:
	print("-1")

# def sol(d, n):
# 	global K
# 	global ans
# 	# print("!")
# 	if d == K:
# 		vis.add(n)
# 		ans.append(n)
# 		return
# 	if n in ans:
# 		ans.remove(n)
# 	for i in range(len(graph[n])):
# 		# print(graph[n][i])
# 		if graph[n][i] not in vis:
# 			# print(f"ans:{ans} / node:{graph[n][i]}")
# 			vis.add(graph[n][i])
# 			sol(d + 1, graph[n][i])

# ans = []
# vis = set()
# vis.add(X)
# for i in range(len(graph[X])):
# 	# print(f"i {i} {graph[X][i]}")
# 	sol(1, graph[X][i])
