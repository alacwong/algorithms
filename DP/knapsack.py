def solve_knapsack(profits, weights, capacity):
    """
    knapsack solution in O(n * c) space
    recurse to get knapsack
    """
    dp = [[0] * (capacity + 1) for _ in range(len(weights))]

    for i in range(1, capacity + 1):
        if i >= weights[0]:
            dp[0][i] = profits[0]

    for i in range(1, len(profits)):
        for j in range(1, capacity + 1):
            if j >= weights[i]:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i]] + profits[i])
            else:
                dp[i][j] = dp[i - 1][j]

    # Backtrack to get knapsack
    knapsack = []
    i, j = len(weights) - 1, capacity
    while dp[i][j] != 0:

        if dp[i][j] == dp[i - 1][j]:
            i, j = i - 1, j
        else:
            knapsack.append(profits[i])
            i, j = i - 1, j - weights[i]

    return knapsack


def solve_knapsack2(profits, weights, capacity):
    """Solve knapsack in O(c) space"""
    dp = [0] * (capacity + 1)

    for i in range(1, capacity + 1):
        if i >= weights[0]:
            dp[i] = profits[0]

    for i in range(1, len(weights)):
        tmp = dp[:]

        for j in range(1, capacity + 1):
            if j >= weights[i]:
                tmp[j] = max(dp[j], dp[j - weights[i]] + profits[i])

        dp = tmp

    return dp[capacity]


def subset_sum(nums, t):

    dp = [[True] + ([False] * t) for _ in nums]

    for i in range(len(nums)):
        for j in range(1, t + 1):
            dp[i][j] = dp[i - 1][j] or (nums[i] <= j and dp[i - 1][j - nums[i]])

    return dp[len(nums) - 1][t]




if __name__ == '__main__':
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
