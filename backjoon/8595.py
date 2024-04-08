import sys
input = sys.stdin.readline

n = int(input())
s = input()

sum = 0
part = 0

for i in range(len(s) - 1):
    # print(part)
    if s[i] >= '0' and s[i] <= '9':
        if part >= 100000:
            continue
        if part != 0:
            part = (part * 10) + int(s[i])
        else:
            part += int(s[i])
    else:
        sum += part
        part = 0
if part > 0:
    sum += part

print(sum)