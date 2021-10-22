"""
Dynamic programming training arc
Problem: Terrible at dp, spams memoization with lru_cache
Goal: See sub problems with dp table
"""

from collections import deque
import random
from matplotlib import pyplot as plt


def bag_of_words(eng_dict, x):
    """
    Give a polynomial-time dynamic programming algorithm that takes as input a string x[1..n]
    and returns the number of different legal divisions of that string
    """

    dp = [0] * (len(x) + 1)
    dp[0] = 1

    for i in range(1, len(x) + 1):
        for j in range(i):
            if x[j:i] in eng_dict:
                dp[i] += dp[j]

    return dp[len(x)]


def path_sum(matrix):
    """
    Find the path sum from (0, 0) => (n - 1, n - 1)
    [1 2
    3 4] -> (1 + 2 + 4) + ( 1 + 3 + 4) => 15

    [1,
    """

    n = len(matrix)
    visited = [[0] * n for _ in matrix]
    visited[0][0] = 1
    dp = [[0] * n for _ in matrix]
    dp[0][0] = matrix[0][0]
    q = deque([(0, 0)])

    while q:
        for _ in range(len(q)):
            x, y = q.popleft()
            for dx, dy in [[0, 1], [1, 0]]:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < n and 0 <= new_y < n:
                    if visited[new_x][new_y] == 0:
                        q.append((new_x, new_y))
                        visited[new_x][new_y] = 1

                    dp[new_x][new_y] += (dp[x][y] + matrix[new_x][new_y])

    return dp[n - 1][n - 1]


def random_matrix(n, k):
    res = []
    for _ in range(n):
        tmp = []
        for _ in range(n):
            tmp.append(random.randint(0, k))
        res.append(tmp)
    return res


if __name__ == '__main__':
    # print(bag_of_words({'a', 'aa', 'aaa'}, 'aaaaaaaa'))
    x = [path_sum(random_matrix(4, 10)) for _ in range(100000)]
    plt.hist(x, bins=50)
    plt.gca().set(title='Frequency Histogram', ylabel='Frequency')
    plt.show()
