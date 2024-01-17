import sys
input = sys.stdin.readline

A, B ,C = list(map(int, input().split()))

def sol(b):
	global A, C
	if b == 1:
		return A % C
	val = sol(b//2)
	if b % 2 == 0:
		return val * val % C
	return val * val % C * A % C

print(sol(B))
