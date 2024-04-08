import sys
input = sys.stdin.readline

n = int(input())
i = 2

while i <= n:
    if (n % i == 0):
        print(i)
        n /= i
        i = 2
    else:
        i += 1
