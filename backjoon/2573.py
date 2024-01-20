import sys, copy
from collections import deque
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

input = sys.stdin.readline

n, m = list(map(int, input().split()))

board = [list(map(int, input().split())) for _ in range(n)]

ans = 0
print(board)

for _ in range(1, 10):
	area = 0
	q = deque()
	board2 = copy.deepcopy(board)
	vis = [[False] * m for _ in range(n)]
	for y in range(n):
		for x in range(m):
			if board[y][x] > 0 and not vis[y][x]:
				print(f" y{y} x{x} / data= {board[y][x]}")
				cnt = 0
				for dir in range(4):
					cy = y + dy[dir]
					cx = x + dx[dir]
					if board[cy][cx] == 0:
						cnt += 1
				if board2[cy][cx] - cnt <= 0:
					board2[cy][cx] = 0
				else:
					board2[cy][cx] -= cnt
				vis[y][x] = True
				area += 1
				q.append((y, x))
				while q:
					cur = q.popleft()
					for dir in range(4):
						ny = cur[0] + dy[dir]
						nx = cur[1] + dx[dir]
						if not vis[ny][nx] and board[ny][nx] > 0:
							cnt = 0
							for dir in range(4):
								cy = ny + dy[dir]
								cx = nx + dx[dir]
								if board[cy][cx] == 0:
									cnt += 1
							if board2[cy][cx] - cnt <= 0:
								board2[cy][cx] = 0
							else:
								board2[cy][cx] -= cnt
							vis[ny][nx] = True
							q.append((ny,nx))
	if area > 1:
		print("!!!!")
		break
	print(board2)
	board = copy.deepcopy(board2)

print(ans)
