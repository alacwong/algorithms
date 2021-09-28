"""
Inversion Count for an array indicates – how far (or close) the array is from being sorted.
If the array is already sorted, then the inversion count is 0, but if the array is sorted in the reverse order,
the inversion count is the maximum.
Formally speaking, two elements a[i] and a[j] form an inversion
if a[i] > a[j] and i < j

Example:

Input: arr[] = {8, 4, 2, 1}
Output: 6

Explanation: Given array has six inversions:
(8, 4), (4, 2), (8, 2), (8, 1), (4, 1), (2, 1).


Input: arr[] = {3, 1, 2}
Output: 2

Explanation: Given array has two inversions:
(3, 1), (3, 2)
"""


def brute_force(arr):
    count = 0
    n = len(arr)

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                count += 1

    return count


def count_inversions(arr):
    return merge_sort(arr, 0, len(arr))


def merge_sort(arr, l, r):
    if l + 1 == r:
        return 0
    else:
        mid = (l + r) // 2

        inversions = merge_sort(arr, l, mid) + merge_sort(arr, mid, r)

        new = []

        i, j = l, mid

        # [1, 3, 5] [2, 4,6]

        while i < mid and j < r:
            if arr[i] <= arr[j]:
                new.append(arr[i])
                i += 1
            else:
                inversions += mid - i
                new.append(arr[j])
                j += 1

        while i < mid:
            new.append(arr[i])
            i += 1

        while j < r:
            new.append(arr[j])
            j += 1

        for i in range(l, r):
            arr[i] = new[i - l]

        return inversions


if __name__ == '__main__':
    test = [8, 4, 2, 1, 10, 12, 3, 4, 19, 7, 12]
    print(brute_force(test))
    print(count_inversions(test))
