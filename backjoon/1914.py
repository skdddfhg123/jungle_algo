N = int(input())
cnt = 0
print(pow(2, N) - 1)

def sol(a, b, n):
	if n == 1:
		print(f"{a} {b}")
	else:
		sol(a, 6 - a - b, n - 1)
		print(f"{a} {b}")
		sol(6 - a - b, b, n - 1)

if N <= 20:
	sol(1,3,N)
