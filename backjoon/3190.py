import sys
input = sys.stdin.readline
from collections import deque
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N = int(input())

board = [[False] * N for _ in range(N)]

for _ in range(int(input())):
	y, x = map(int,input().split())
	board[x - 1][y - 1] = True

direction = deque()
for _ in range(int(input())):
	t, d = list(input().split())
	direction.append((int(t), d))

t = 0
dir = 0
q = deque()
q.append((1, 1))
while 1:
	t += 1
	cur = q[0]
	nx = cur[0] + dx[dir]
	ny = cur[1] + dy[dir]
	if (nx, ny) in q or nx < 1 or ny < 1 or nx > N or ny > N:
		break
	q.appendleft((nx, ny))
	if board[nx - 1][ny - 1]:
		board[nx - 1][ny - 1] = False
	else:
		q.pop()
	if direction and t == direction[0][0]:
		if direction[0][1] == "D":
			dir = (dir + 1) % 4
		elif direction[0][1] == "L":
			dir = (dir - 1) % 4
		direction.popleft()

print(t)
