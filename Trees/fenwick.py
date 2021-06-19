"""
Fenwick tree useful for computing prefix sums in logn time
"""


class Fenwick:

    def update(self, index: int, value) -> None:
        while index < len(self.tree):
            self.tree[index] += value
            index += index & -index

    def query(self, index):
        ans = 0

        while index > 0:
            ans += self.tree[index]
            index -= index & -index
        return ans

    def __init__(self, arr):
        self.tree = [0] * (len(arr) + 1)
        for i in range(1, len(arr)):
            self.update(i, arr[i])


if __name__ == '__main__':
    fenwick = Fenwick([0, 1, 2, 3, 4, 5, 6])
    print(fenwick.query(3))
