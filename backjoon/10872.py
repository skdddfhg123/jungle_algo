n = int(input())

def sol(i):
	if i == 0:
		return 1
	return sol(i - 1) * i

print(sol(n))
