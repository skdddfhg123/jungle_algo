import sys
input = sys.stdin.readline

a,b,v = list(map(int, input().split()))

day = (v - b) // (a - b)
mod = (v - b) % (a - b)

if mod == 0:
	print(day)
else:
	print(day + 1)