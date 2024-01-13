import sys
from functools import cmp_to_key
input = sys.stdin.readline

data = []
for _ in range(int(input())):
	data.append(input())

def cmp(a, b):
    if len(a) < len(b):
        return -1
    elif len(a) > len(b):
        return 1
    else:
        if a < b:
            return -1
        elif a > b:
            return 1
        else:
            return 0

data = sorted(set(data), key=cmp_to_key(cmp))

for i in range(len(data)):
    print(data[i],end='')
