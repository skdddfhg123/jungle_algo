import sys
input = sys.stdin.readline

vis = [False] * 11
ans = 10000001
N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

def sol(a, b, start, n, t):
    global vis
    global ans
    global arr
    a = b
    if n == N - 1 and arr[a][start] != 0:
        # print(t + arr[a][start])
        ans = min(ans, t + arr[a][start])
        return
    for i in range(N):
        if not vis[i] and arr[a][i] != 0:
            # print(f'a:{a},b:{i},start:{start},n:{n+1}t:{t+arr[a][i]}')
            vis[i] = True
            sol(a, i, start,n + 1, t + arr[a][i])
            vis[i] = False

for i in range(N):
    if not vis[i]:
        vis[i] = True
        sol(i, i, i, 0, 0)
        vis[i] = False

print(ans)
