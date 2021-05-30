"""
bisect an array
"""
import math


def bisect_left(arr, x, low=None, hi=None, ):
    """ return index to be for array arr
    [2,4,9, 11, 15]
    13
    ->
    4 bc we insert x after the third element 11
    """

    if low is None or hi is None:
        low, hi = 0, len(arr)

    #
    while low < hi:
        mid = int((low + hi) / 2)
        if arr[mid] < x:
            low = mid + 1
        else:
            hi = mid

    return low


def bisect_right(arr, x, low=None, hi=None, ):
    if low is None or hi is None:
        low, hi = 0, len(arr)

        while low < hi:
            mid = int((low + hi) / 2)
            if arr[mid] <= x:
                low = mid + 1
            else:
                hi = mid

        return low


def bisect_recurse(arr, x, low=None, hi=None):
    """
    array bisection recursively
    """

    if low is None or hi is None:
        low, hi = 0, len(arr)

    if low >= hi:
        return hi
    else:
        mid = int((low + hi) / 2)
        if arr[mid] < x:
            return bisect_recurse(arr, x, mid + 1, hi)
        else:
            return bisect_recurse(arr, x, low, mid)




if __name__ == '__main__':
    array = [1, 2, 3, 3, 3, 6, 7, 10, 12]
    print(bisect_recurse(array, 19))
