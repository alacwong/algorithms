import random


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


def get_tests(num_tests, n):
    tests = []

    for _ in range(num_tests):
        preferences = [
            [i + 1 for i in range(n)] for _ in range(3)
        ]

        for i in range(3):
            random.shuffle(preferences[i])

        tests.append(preferences)

    return tests


def brute_force(preferences):
    ans = -1

    for i, p in enumerate(preferences[0]):
        x, y = preferences[1].index(p), preferences[2].index(p)
        if len(set(preferences[preferences[1][:x]] + preferences[2][:y])) == x + y:
            return p

    return ans


def format_test(test):
    for i in range(3):
        print(test[i])


if __name__ == '__main__':

    tests = get_tests(20, 10)

    for test in tests:
        format_test(test)
        print(solve(test))

