import sys
input = sys.stdin.readline

n = int(input())
s = int(input())

sum = 0

while s:
    sum += int(s % 10)
    s = s // 10

print(sum)