import sys, heapq
from collections import deque
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n = int(input())

map = [list(map(int, input().strip())) for _ in range(n)]
vis = [[False] * n for _ in range(n)]
hq = []

heapq.heappush(hq, [0, 0, 0])
ans = n * n
vis[0][0] = True
while hq:
	cnt, y, x = heapq.heappop(hq)
	if y == n - 1 and x == n - 1:
		ans = min(ans, cnt)
	for dir in range(4):
		ny = y + dy[dir]
		nx = x + dx[dir]
		if ny < 0 or ny >= n or nx < 0 or nx >= n:
			continue
		if vis[ny][nx] == False:
			vis[ny][nx] = True
			if map[ny][nx] == 1:
				heapq.heappush(hq, [cnt, ny, nx])
			else:
				heapq.heappush(hq, [cnt + 1, ny, nx])

print(ans)

