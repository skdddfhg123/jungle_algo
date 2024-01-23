import sys, copy
from collections import deque
input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n, m = list(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(n)]

ans = 0
flag = False
while 1:
	o_check = 0
	area = 0
	q = deque()
	board2 = copy.deepcopy(board)
	# print(f"board1\n{board}\nboard2\n{board2}")
	vis = [[False] * m for _ in range(n)]
	for y in range(n):
		for x in range(m):
			if board2[y][x] > 0 and not vis[y][x]:
				# print(f" y{y} x{x} / data= {board2[y][x]}")
				cnt = 0
				for dir in range(4):
					cy = y + dy[dir]
					cx = x + dx[dir]
					if board[cy][cx] == 0:
						cnt += 1
				if board2[y][x] - cnt <= 0:
					board2[y][x] = 0
				else:
					board2[y][x] -= cnt
				vis[y][x] = True
				area += 1
				if area > 1:
					break
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
									# print(f"cy{cy} cx{cx}")
									cnt += 1
							if board2[ny][nx] - cnt <= 0:
								board2[ny][nx] = 0
							else:
								board2[ny][nx] -= cnt
							# print(f"x{nx} y{ny} board: {board2[ny][nx]}")
							vis[ny][nx] = True
							q.append((ny,nx))
			elif board2[y][x] == 0:
				o_check += 1
	if area > 1:
		flag = True
		# print("!!!!")
		break
	elif o_check == n * m:
		break
	board = board2[:]
	ans+=1
if flag:
	print(ans)
else: 
	print("0")