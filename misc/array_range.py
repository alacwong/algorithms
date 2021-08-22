from bisect import bisect_left, bisect_right
import random


def solve(arr, l, r):
    """
    Return number of elements in arr within range l, r

    [1,4,6,9, 10], 3,7 -> 2
    len([4, 6]) = 2
    """
    left = bisect_left(arr, l)
    right = bisect_right(arr, r)
    return right - left


def verify(arr, l, r):
    count = 0

    for elem in arr:
        if l <= elem <= r:
            count += 1

    return count


def test(t=20, n=100, r=100):
    for _ in range(t):
        arr = sorted([random.randint(0, r) for _ in range(n)])
        a, b = sorted([random.randint(0, 100), random.randint(0, 100)])
        ans = verify(arr, a, b)
        res = solve(arr, a, b)
        if ans == res:
            print(f'Pass')
        else:
            print(f'Fail {ans} != {res} for {arr} l={a} r={b}')


if __name__ == '__main__':
    test()
