from bisect import bisect_left
from itertools import accumulate


def find_count(arr):
    prefix = list(accumulate(arr))

    ans = 0

    for idx, a in enumerate(prefix):
        lower = bisect_left(prefix, 2 * a, idx)
        mid = (prefix[-1] - prefix[idx]) / 2
        upper = bisect_left(prefix, mid, idx)

        print(prefix[idx], prefix[lower] - prefix[idx], prefix[-1] - prefix[lower])

        print(prefix[idx], prefix[upper] - prefix[idx], prefix[-1] - prefix[upper])

        if upper > lower:
            ans += upper - lower
        else:
            break

    return ans


def findCount(arr, n):
    # Stores the prefix sums
    prefix_sum = [0 for x in range(n)]
    prefix_sum[0] = arr[0]

    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i]

    # Stores the suffix sums
    suffix_sum = [0 for x in range(n)]

    suffix_sum[n - 1] = arr[n - 1]

    for i in range(n - 2, -1, -1):
        suffix_sum[i] = suffix_sum[i + 1] + arr[i]

    s = 1
    e = 1
    curr_subarray_sum = 0
    count = 0

    # Traverse the given array
    while (s < n - 1 and e < n - 1):

        # Updating curr_subarray_sum until
        # it is less than prefix_sum[s-1]
        while (e < n - 1 and
               curr_subarray_sum < prefix_sum[s - 1]):
            curr_subarray_sum += arr[e]
            e += 1

        if (curr_subarray_sum <= suffix_sum[e]):
            # Increase count
            count += 1

        # Decrease curr_subarray_sum by arr[s[]
        curr_subarray_sum -= arr[s]
        s += 1

    # Return count
    return count


def vassos(fires, firefighters, d):
    i = j = 0

    fires = sorted(map(lambda x: (x[1], x[0]), enumerate(fires)))
    firefighters = sorted(map(lambda x: (x[1], x[0]), enumerate(firefighters)))
    ans = []

    while i < len(fires) and j < len(firefighters):
        fire, idx = fires[i]
        firefighter, idy = firefighters[j]

        if abs(fire - firefighter) <= d:
            ans.append((idx, idy))
            i, j = i + 1, j + 1
        elif fire < firefighter:
            i += 1
        else:
            j += 1

    return ans


def generate_parenthesis(n):
    from collections import defaultdict
    ans = defaultdict(set, {1: {'()', '[]'}})

    for i in range(2, n + 1):
        for parenthesis in ans[i - 1]:
            ans[i].add(f'({parenthesis})')
            ans[i].add(f'[{parenthesis}]')

        for j in range(1, i):
            for paran1 in ans[j]:
                for paran2 in ans[i - j]:
                    ans[i].add(paran1 + paran2)

    return list(ans[n])


def generate_parenthesis2(n, m):
    brackets = generate_parenthesis(n + m)
    ans = []
    for bracket in brackets:
        if bracket_counter(bracket) == n:
            ans.append(bracket)
    return ans


def bracket_counter(s):
    count = 0
    for char in s:
        if char == '(':
            count += 1
    return count


if __name__ == '__main__':
    print(vassos([1, 3, 5, 9, 12, 12, 15, 16], [4, 9, 11, 11, 11, 11], 3))
    # print(len(generate_parenthesis2(5, 5)))
