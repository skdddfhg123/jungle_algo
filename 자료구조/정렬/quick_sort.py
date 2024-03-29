# [Do it! 실습 6-10] 퀵 정렬 알고리즘 구현

from typing import MutableSequence

def qsort(a: MutableSequence, left: int, right: int) -> None:
    """a[left] ~ a[right]를 퀵 정렬"""
    if left < right:
        pl = left                   # 왼쪽 커서
        pr = right                  # 오른쪽 커서
        x = a[(left + right) // 2]  # 피벗(가운데 요소)
        print(f'\nleft:{pl} right:{pr} x:{x}')
        while pl <= pr:
            while a[pl] < x:
                pl += 1
                print(f'값:{a[pl]} / 인덱스pl:{pl}')
            while a[pr] > x:
                pr -= 1
                print(f'값:{a[pr]} / 인덱스pr:{pr}')
            if pl <= pr:
                print(f'값 교환:{a[pl]} {a[pr]} / 인덱스 pl:{pl},pr:{pr}')
                a[pl], a[pr] = a[pr], a[pl]
                pl += 1
                pr -= 1
                print(f"교차{pl} {pr}")

        qsort(a, left, pr)
        qsort(a, pl, right)

def quick_sort(a: MutableSequence) -> None:
    """퀵 정렬"""
    qsort(a, 0, len(a) - 1)

if __name__ == '__main__':
    print('퀵 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num   # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    quick_sort(x)      # 배열 x를 퀵 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')