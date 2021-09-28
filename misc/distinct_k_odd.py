"""
Compute number of distinct subarray(s) with at most k odd elemnts
"""
from collections import deque
from typing import Tuple


def distinct(nums: Tuple[int], k: int):
    q = deque([])
    s = set()
    stop = -1

    for idx, num in enumerate(nums):

        if num % 2 == 1:
            q.append(idx)
            if len(q) > k:
                stop = q.popleft()

        for j in range(idx, stop, -1):
            s.add(nums[j:idx + 1])
            
    return len(s)


if __name__ == '__main__':
    print(distinct(tuple([6, 1, 3, 2]), 1))
    print(distinct(tuple([2, 2, 1, 2, 3, 3]), 2))

