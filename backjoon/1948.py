import sys, heapq
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
graph2 = [[] for _ in range(n + 1)]
graph_check = [[] for _ in range(n + 1)]
check = [0] * (n + 1)
indegree = [0] * (n + 1)


for _ in range(m):
	s, e, c = list(map(int, input().split()))
	graph[s].append((c, e))
	indegree[e] += 1

hq = []

S, E = list(map(int, input().split()))
# for i in range(1, n + 1):
# 	if indegree[i] == 0:
heapq.heappush(hq, (0, S))

while hq:
	cost, cur = heapq.heappop(hq)
	for w, next in graph[cur]:
		total = -w + check[cur]
		if total < check[next]:
			check[next] = total
			heapq.heappush(hq, (total, next))

print(check)



