import sys
input = sys.stdin.readline

x, y = list(map(int, input().split()))

x_c = []
y_c = []
for _ in range(int(input())):
	d, n = list(map(int, input().split()))
	if d == 0:
		y_c.append(n)
	else:
		x_c.append(n)

x_c.sort()
y_c.sort()
if x_c:
	x_max = max(x_c[0], x - x_c[len(x_c) - 1])
else:
	x_max = x
for i in range(1, len(x_c)):
	if x_c[i] - x_c[i-1] > x_max:
		x_max = x_c[i] - x_c[i-1]
if y_c:
	y_max = max(y_c[0], y - y_c[len(y_c) - 1])
else:
	y_max = y
for i in range(1, len(y_c)):
	if y_c[i] - y_c[i-1] > y_max:
		y_max = y_c[i] - y_c[i-1]

print(x_max * y_max)
