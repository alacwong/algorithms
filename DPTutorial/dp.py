"""
Simple Tutorial for Dynamic programming
"""

import timeit


def fib_recursion(n: int) -> int:
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib_recursion(n - 1) + fib_recursion(n - 2)


d = {1: 1, 2: 1}


def fib_memo(n: int) -> int:
    if n not in d:
        d[n] = fib_memo(n - 1) + fib_memo(n - 2)
    return d[n]


def fib_tabulation(n: int) -> int:
    if n == 0:
        return 1
    elif n == 1:
        return 1

    dp = [0] * n
    dp[0] = 1
    dp[1] = 2

    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n - 1]


def fib_tabulation_cs(n: int) -> int:
    """
    @author Raymond Chen / cheryl
    precondition n > 0
    :param n:
    :return:
    """

    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        i, j = 1, 1
        for index in range(1, n):
            i, j, = j, i + j
    return j


def compare_speed(n: int, f1, f2):
    for i in range(1, n):
        def wrapper1():
            f1(i)

        def wrapper2():
            f2(i)

        speed1 = timeit.timeit(wrapper1, number=100)
        speed2 = timeit.timeit(wrapper2, number=100)
        print(f'{f1.__name__}({i}): {speed1} | {f2.__name__}({i}): {speed2}')


def speed(n: int, f):
    for i in range(1, n):
        def wrapper():
            f(i)

        runtime = timeit.timeit(wrapper, number=100)
        print(f'{f.__name__}({i}): {runtime}')


if __name__ == '__main__':
    for num in range(1, 10):
        print(fib_tabulation_cs(num))


