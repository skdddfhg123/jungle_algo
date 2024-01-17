import sys
input = sys.stdin.readline

x, y, w, h = list(map(int, input().split()))

ret = min(w - x, h - y, x, y)
print(ret)
