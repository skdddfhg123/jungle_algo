import math

def prime_check(x):
	for i in range(2, int(math.sqrt(x)) + 1):
		if x % i == 0:
			return False
	return True

all_prime = []

check = [False] * 10001

for i in range(2, 10000):
	if prime_check(i):
		check[i] = True
		all_prime.append(i)

for _ in range(int(input())):
	num = int(input())
	cmp = num // 2
	a = 0
	b = 10000
	for i in range(len(all_prime)):
		if cmp < all_prime[i]:
			break
		if check[num - all_prime[i]]:
			if all_prime[i] - (num - all_prime[i]) < b - a:
				a = all_prime[i]
				b = num - all_prime[i]
	print(f'{a} {b}')
