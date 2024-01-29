import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
graph2 = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for _ in range(m):
	s, e, c = list(map(int, input().split()))
	graph[s].append((c, e))
	graph2[e].append((c, s))
	indegree[e] += 1

S, E = list(map(int, input().split()))
q = deque()
q.append(S)
dist = [0] * (n + 1)

top_sort_list = [-1] * (n + 1)
top_sort_idx = 0

graph_check = [[] for _ in range(n + 1)]

while q:
	cur = q.popleft()
	top_sort_list[top_sort_idx] = cur
	top_sort_idx += 1

	max_cost = 0
	for cost, prev in graph2[cur]:
		total = cost + dist[prev]
		if total > max_cost:
			max_cost = total
			graph_check[cur] = [prev]
		elif total == dist[prev]:
			graph_check[cur].append(prev)
	dist[cur] = max_cost

	for cost, next in graph[cur]:
		indegree[next] -= 1
		if indegree[next] == 0:
			q.append(next)

# cnt = 0
q.append(E)
check = [0] * (n + 1)
vis = set()
while q:
	cur = q.popleft()
	# print(cur)
	for prev in graph_check[cur]:
		check[prev] += 1 + check[cur]
		check[cur] = 0
		if prev not in vis:
			vis.add(prev)
			q.append(prev)

print(dist[E])
print(check)

# print(check)



