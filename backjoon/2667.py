import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N = int(input())
board = [list(map(int,input().strip())) for _ in range(N)]
vis = [[False] * N for _ in range(N)]

# print(board)
# print(vis)

ans = []
q = deque()
for i in range(N):
	for j in range(N):
		if not vis[i][j] and board[i][j] == 1:
			q.append((i, j))
			vis[i][j] = True
			cnt = 1
			while q:
				cy, cx = q.popleft()
				for dir in range(4):
					ny = cy + dy[dir]
					nx = cx + dx[dir]
					if ny < 0 or ny >= N or nx < 0 or nx >= N:
						continue
					if not vis[ny][nx] and board[ny][nx] == 1:
						vis[ny][nx] = True
						cnt += 1
						q.append((ny, nx))
			ans.append(cnt)

ans.sort()

print(len(ans))
for i in range(len(ans)):
	print(ans[i])
# print(*ans)
