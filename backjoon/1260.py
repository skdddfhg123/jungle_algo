import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[False] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
	a, b = map(int, input().split())
	graph[a][b] = True
	graph[b][a] = True
vis1 = [False] * (N + 1)
vis2 = [False] * (N + 1)
ans1 = []
ans2 = []
def dfs(V):
	vis1[V] = True
	ans1.append(V)
	for i in range(1, N + 1):
		if not vis1[i] and graph[V][i]:
			dfs(i)
def bfs(V):
	q = deque([V])
	vis2[V] = True
	while q:
		V = q.popleft()
		ans2.append(V)
		for i in range(1, N + 1):
			if not vis2[i] and graph[V][i]:
				q.append(i)
				vis2[i] = True
dfs(V)
bfs(V)
print(" ".join(map(str, ans1)))
print(" ".join(map(str, ans2)))


# N, M, V = list(map(int, input().split()))

# nodes = [list(map(int, input().split())) for _ in range(M)]

# nodes.sort()

# def find_node(target):
# 	ret = []
# 	for a, b in nodes:
# 		if target == a:
# 			ret.append(b)
# 		elif target == b:
# 			ret.append(a)
# 	return ret

# def dfs(start):
# 	s = [start]
# 	vis = set()
# 	ret = []
# 	s.append(start)
# 	while s:
# 		v = s.pop()
# 		if v not in vis:
# 			ret.append(v)
# 			vis.add(v)
# 			add_v = find_node(v)
# 			s.extend(add_v[::-1])
# 	return ret

# def bfs(start):
# 	q = deque()
# 	vis = set()
# 	ret = []
# 	q.append(start)
# 	vis.add(start)
# 	while q:
# 		v = q.popleft()
# 		ret.append(v)
# 		add_v = find_node(v)
# 		for neighbor in add_v:
# 			if neighbor not in vis:
# 				vis.add(neighbor)
# 				q.append(neighbor)
# 	return ret


# print(" ".join(map(str, dfs(V))))
# print(" ".join(map(str, bfs(V))))
