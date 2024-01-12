n = int(input())

def fun(i):
	if i == 0:
		return 1
	return fun(i - 1) * i

print(fun(n))
