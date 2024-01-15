import sys
input = sys.stdin.readline
from collections import defaultdict

check = defaultdict(bool)

N = int(input())
arr = list(map(int, input().split()))

for i in range(N):
	check[arr[i]] = True

cmp_n = int(input())
cmp = list(map(int, input().split()))

for i in range(cmp_n):
	if check[cmp[i]] == True:
		print('1')
	else:
		print('0')
