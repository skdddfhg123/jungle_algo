import sys
input = sys.stdin.readline
from collections import deque
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N = int(input())

board = [list([False] * N) for _ in range(N)]

for _ in range(int(input())):
	x, y = list(input().split())
	board[x][y] = True

direction = []
for _ in range(int(input())):
	t, d = list(input().split())
	direction.append((t, d))

q = deque()

def dir_change(flag)