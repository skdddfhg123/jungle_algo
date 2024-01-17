import sys, heapq
input = sys.stdin.readline

lh = []
rh = []

for _ in range(int(input())):
	data = int(input())
	if len(lh) == len(rh):
		heapq.heappush(lh, -data)
	else:
		heapq.heappush(rh, data)
	if rh and rh[0] < -lh[0]:
		l_value = heapq.heappop(lh)
		r_value = heapq.heappop(rh)
		heapq.heappush(lh, -r_value)
		heapq.heappush(rh, -l_value)
	print(-lh[0])