import sys
input = sys.stdin.readline
import heapq

hq = []


for _ in range(int(input())):
	data = int(input())
	if data == 0:
		if hq:
			print(-heapq.heappop(hq))
		else:
			print("0")
	else:
		heapq.heappush(hq, -data)
