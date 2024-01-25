import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 1, 0, -1, 0, 0]
dy = [1, 0, -1, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

M, N, H = list(map(int,input().split()))
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
vis = [[[False] * M for _ in range(N)] for _ in range(H)]

# print(arr)
# print(vis)
q = deque()
for z in range(H):
	for y in range(N):
		for x in range(M):
			if arr[z][y][x] == 1:
				q.append((z, y, x))
				vis[z][y][x] = True

while q:
	cz, cy, cx = q.popleft()
	for dir in range(6):
		nz = cz + dz[dir]
		ny = cy + dy[dir]
		nx = cx + dx[dir]
		if nz < 0 or nz >= H or ny < 0 or ny >= N or nx < 0 or nx >= M:
			continue
		if arr[nz][ny][nx] == 0 and vis[nz][ny][nx] == False:
			vis[nz][ny][nx] = True
			arr[nz][ny][nx] = arr[cz][cy][cx] + 1
			q.append((nz, ny, nx))

# print(arr)
flag = False
ans = 0
for z in range(H):
	for y in range(N):
		for x in range(M):
			if arr[z][y][x] == 0:
				flag = True
			else:
				ans = max(ans, arr[z][y][x])

if flag:
	print("-1")
else:
	print(ans-1)