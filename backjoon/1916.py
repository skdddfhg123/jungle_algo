import sys, heapq
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
	a,b,c = list(map(int,input().split()))
	graph[a].append([b, c])

S, E = list(map(int, input().split()))
costs = [1e9 for _ in range(N + 1)]
hq = []
costs[S] = 0
heapq.heappush(hq, [0, S])

while hq:
	cost, nodes = heapq.heappop(hq)
	if costs[nodes] < cost:
		continue
	for v, c in graph[nodes]:
		total = cost + c
		if total >= costs[v]:
			continue
		costs[v] = total
		heapq.heappush(hq, [total, v])

print(costs[E])
