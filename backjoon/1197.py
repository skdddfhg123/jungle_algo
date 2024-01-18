import sys
input = sys.stdin.readline

V, E = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(E)]

print(arr[0][0])