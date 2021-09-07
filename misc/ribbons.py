def cutTheRibbons(a, k):
    # [5, 2, 7, 4, 16]

    """
    # [5, 2, 7, 4, 16] => 2

    lower = 4 = 7

    6 => 1 + 2 = 3

    """

    upper = 1
    while cut(a, upper) >= k:
        upper *= 2

    lower = upper // 2

    while lower + 1 < upper:

        mid = (upper + lower) // 2
        if cut(a, mid) >= k:
            lower = mid
        else:
            upper = mid

    return lower


def cut(a, k):
    ribbons = 0
    for e in a:
        ribbons += e // k

    return ribbons