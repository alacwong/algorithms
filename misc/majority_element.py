def majority_element(nums):
    """
    Given a non negative array of
    return num st num is at least n/4 positions
    """

    d1 = d2 = d3 = -1
    c1 = c2 = c3 = 0

    for num in nums:

        if num == d1:
            c1 += 1
        elif num == d2:
            c2 += 1
        elif num == d3:
            c3 += 1
        elif d1 == -1:
            d1, c1 = num, 1
        elif d2 == -1:
            d2, c2 = num, 1
        elif d3 == -1:
            d3, c3 = num, 1
        else:
            c1 -= 1
            c2 -= 1
            c3 -= 1

    for candidate in [d1, d2, d3]:
        count = 0
        for num in nums:
            if num == candidate:
                count += 1

        if count > len(nums) / 4:
            return candidate

    return -1


if __name__ == '__main__':
    print(majority_element([1, 2, 3, 3, 4]))
    print(majority_element([4, 2, 3, 3, 4, 4]))
    print(majority_element([1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
