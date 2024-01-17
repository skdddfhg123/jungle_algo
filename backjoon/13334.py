import sys, heapq
from collections import defaultdict

input = sys.stdin.readline

check = defaultdict(bool)
roads = []

for _ in range(int(input())):
	a, b = list(map(int, input().split()))
	roads.append((max(a, b), min(a, b)))
L = int(input())
roads.sort()
hq = []
ans = 0
for road in roads:
	if road[0] - road[1] <= L:
		heapq.heappush(hq, road[1])
	else:
		continue

	while hq:
		start = hq[0]
		if road[0] - start > L:
			heapq.heappop(hq)
		else:
			break
	ans = max(len(hq), ans)
print(ans)
