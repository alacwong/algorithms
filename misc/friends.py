def solve(preferences):
    n = len(preferences[0])
    friends = [set(), set(), set()]
    seen = set()
    ans = -1

    for j in range(n):
        cont = False

        for i in range(3):
            if ans in friends[i]:
                continue
            else:
                cont = True
                if preferences[i][j] in seen:
                    if ans == -1:
                        ans = preferences[i][j]
                    elif ans != preferences[i][j]:
                        return -1

                friends[i].add(preferences[i][j])

        for i in range(3):
            if ans in friends[i]:
                continue
            else:
                seen.add(preferences[i][j])

        if not cont:
            break

    return ans


if __name__ == '__main__':

    tests = [
        [
            [1, 2, 3, 4],
            [3, 1, 2, 4],
            [1, 2, 4, 3]
        ]
    ]

    for test in tests:
        print(solve(test))
