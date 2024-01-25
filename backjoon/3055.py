import sys
from collections import deque
input = sys.stdin.readline

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

R, C = list(map(int, input().split()))

map = [list(input().strip()) for _ in range(R)]
vis = [[False] * C for _ in range(R)]

q = deque()
water_q = deque()

for y in range(R):
	for x in range(C):
		if map[y][x] == 'S':
			q.append((y, x, 1))
			map[y][x] = 0
			vis[y][x] = True
		elif map[y][x] == 'D':
			goal_y = y
			goal_x = x
			map[y][x] = -2
		elif map[y][x] == '*':
			map[y][x] = 1
			water_q.append((y, x))
		elif map[y][x] == 'X':
			map[y][x] = -1
		elif map[y][x] == '.':
			map[y][x] = 0

while water_q:
	cy, cx = water_q.popleft()
	for dir in range(4):
		ny = cy + dy[dir]
		nx = cx + dx[dir]
		if nx < 0 or nx >= C or ny < 0 or ny >= R:
			continue
		if map[ny][nx] == 0:
			map[ny][nx] = map[cy][cx] + 1
			water_q.append((ny, nx))

ans = 0
while q:
	cy, cx, step = q.popleft()
	if cy == goal_y and cx == goal_x:
		ans = step
	for dir in range(4):
		ny = cy + dy[dir]
		nx = cx + dx[dir]
		if nx < 0 or nx >= C or ny < 0 or ny >= R or map[ny][nx] == 'X':
			continue
		if (map[ny][nx] > step + 1 or map[ny][nx] == -2 or map[ny][nx] == 0) and vis[ny][nx] == False:
			vis[ny][nx] = True
			q.append((ny, nx, step + 1))

if ans:
	print(ans - 1)
else:
	print("KAKTUS")