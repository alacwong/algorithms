def distance_metric(nums):
    """
    1, 2, 1, 1, 2, 3

    2
    :param nums:
    :return:
    """
    d = {}
    ans = 0

    for idx, num in enumerate(nums):
        if num not in d:
            d[num] = (idx, 1, 0)
        else:
            print(d)
            idy, count, val = d.get(num)
            new_val = (idx - idy) * count + val
            d[num] = (idx, count + 1, new_val)
            ans += new_val
            print(new_val, num, idx)
    return ans


if __name__ == '__main__':
    print(distance_metric([1, 2, 1, 1, 2, 3]))
