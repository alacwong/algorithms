

def solve(queries, a, b):

    """
    query in the form of
    [1, i, x] -> set a[i] to x
    [0, x] -> count i, j st a[i] + b[j] = x
    :param queries:  list of queries
    :param a:
    :param b:
    :return: array b
    """

    d: dict = {}

    for numa in a:
        for numb in b:
            d[numa + numb] = d.get(numa + numb, 0) + 1

    # Keep track of diffs
    original = {}
    for i in range(len(a)):
        original[i] = {}
        for numb in b:
            original[i][a[i] + numb] = original[i].get(a[i] + numb, 0) + 1

    diff = {}

    for query in queries:
        if len(query) == 3:
            _, i, x = query
            diff[i] = x
        else:
            _, x = query

            # Consolidate queries
