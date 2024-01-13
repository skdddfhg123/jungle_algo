import sys
input = sys.stdin.readline

heights = []
for _ in range(9):
    n = int(input())
    heights.append(n)

total_height = sum(heights)

heights.sort()

i = 0
j = 8

while i < j:
    current_sum = heights[i] + heights[j]
    
    if current_sum == total_height - 100:
        for k in range(9):
            if k != i and k != j:
                print(heights[k])
        break
    elif current_sum < total_height - 100:
        i += 1
    else:
        j -= 1