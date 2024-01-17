import sys
input = sys.stdin.readline

stack = []

n = int(input())

for _ in range(n):
	data = input().split()
	if data[0] == "push":
		stack.append(data[1])
	elif data[0] == "pop":
		if len(stack) >= 1:
			print(stack.pop())
		else:
			print("-1")
	elif data[0] == "size":
		print(len(stack))
	elif data[0] == "empty":
		if len(stack):
			print("0")
		else:
			print("1")
	elif data[0] == "top":
		if len(stack):
			print(stack[-1])
		else:
			print("-1")

