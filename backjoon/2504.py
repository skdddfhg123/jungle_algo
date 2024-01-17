import sys
from collections import deque
input = sys.stdin.readline

data = input()

flag = False
sum = 0
num = 1
stack = []
for i in range(len(data)):
	
	if data[i] == '(':
		num *= 2
		stack.append(data[i])
	elif data[i] == '[':
		num *= 3
		stack.append(data[i])
	elif data[i] == ')':
		if not stack or stack[-1] == '[':
			sum = 0
			break
		if data[i - 1] == '(':
			sum += num
		stack.pop()
		num //= 2
	else:
		if not stack or stack[-1] == '(':
			sum = 0
			break
		if data[i - 1] == '[':
			sum += num
		stack.pop()
		num //= 3
	# print(f"{data[i]} num:{num}/sum:{sum}")

if stack:
	print("0")
else:
	print(sum)

