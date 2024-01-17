from collections import deque
import sys
input = sys.stdin.readline
q = deque()

for _ in range(int(input())):
	data = list(input().split())
	if data[0] == "push":
		q.append(int(data[1]))
	elif data[0] == "pop":
		if len(q):
			print(q.popleft())
		else:
			print("-1")
	elif data[0] == "size":
		print(len(q))
	elif data[0] == "empty":
		if q:
			print("0")
		else:
			print("1")
	elif data[0] == "front":
		if q:
			print(q[0])
		else:
			print("-1")
	elif data[0] == "back":
		if q:
			print(q[-1])
		else:
			print("-1")