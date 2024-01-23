import random
import time

a = list(range(100000))

# sort 함수
time_1 = []
for i in range(100):
    random.shuffle(a)
    start = time.time()
    a.sort()
    time_1.append(time.time() - start)

print(sum(time_1) / 100)

# sorted 함수
time_2 = []
for i in range(100):
    random.shuffle(a)
    start = time.time()
    a = sorted(a)
    time_2.append(time.time() - start)

print(sum(time_2) / 100)

# 직접 구현한 quick_sort 함수
def q_sort(data, left, right):
    if left < right:
        pl = left
        pr = right
        x = data[(left + right) // 2]

        while pl <= pr:
            while data[pl] < x: pl+=1
            while data[pr] > x: pr-=1
            if pl <= pr:
                data[pl], data[pr] = data[pr], data[pl]
                pl+=1
                pr-=1
        
        q_sort(data, left, pr)
        q_sort(data, pl, right)


time_3 = []
for i in range(100):
    a = list(range(100000))
    random.shuffle(a)
    start = time.time()
    q_sort(a, 0, len(a)-1)
    time_3.append(time.time() - start)

print(sum(time_3) / 100)
# 직접 구현한 quick_sort 함수
def sort3(data, idx1, idx2, idx3):
    if data[idx2] < data[idx1]: data[idx2], data[idx1] = data[idx1], data[idx2]
    if data[idx3] < data[idx2]: data[idx3], data[idx2] = data[idx2], data[idx3]
    if data[idx2] < data[idx1]: data[idx2], data[idx1] = data[idx1], data[idx2]
    return idx2

def insertion_sort(data , left, right):
    for i in range(left + 1, right + 1):
        j = i
        tmp = data[i]
        while j > 0 and data[j - 1] > tmp:
            data[j] = data[j - 1]
            j -= 1
        data[j] = tmp

def q_sort2(data, left, right):
    if right - left < 9:
        insertion_sort(data, left, right)
    else:
        if left < right:
            pl = left
            pr = right
            m = sort3(data, pl, (pl + pr) // 2, pr)
            x = data[m]

            data[m], data[pr - 1] = a[pr -1], data[m]
            pl += 1
            pr -= 2
            while pl <= pr:
                while data[pl] < x: pl+=1
                while data[pr] > x: pr-=1
                if pl <= pr:
                    data[pl], data[pr] = data[pr], data[pl]
                    pl+=1
                    pr-=1
            
            q_sort2(data, left, pr)
            q_sort2(data, pl, right)


time_4 = []
for i in range(100):
    a = list(range(100000))
    random.shuffle(a)
    start = time.time()
    q_sort2(a, 0, len(a)-1)
    time_4.append(time.time() - start)

print(sum(time_4) / 100)

