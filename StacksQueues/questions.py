from StacksQueues.stack import AbstractStack
from copy import copy


class ThreeStack:
    """
    Implement 3 stacks using an array
    """

    def __init__(self):
        self.start = {
            0: 0,
            1: 3,
            2: 6
        }

        self.range = {
            0: 3,
            1: 3,
            2: 3,
        }

        self.counts = {
            0: 0,
            1: 3,
            2: 6
        }

        self.array = [0] * 9

    def push(self, index: int, val: int) -> None:
        new_index = self.start[index] + self.counts[index]
        self.array[new_index] = val
        self.counts[index] += 1
        self._reallocate()

    def pop(self, index: int) -> int:
        if self.counts[index] > 0:
            popped = self.peek(index)
            self.counts[index] -= 1
            return popped
        else:
            raise IndexError('No element can be popped')

    def peek(self, index: int) -> int:
        return self.array[self.start[index] + self.counts[index]]

    def _reallocate(self):
        """
        Reallocate array resources through index shifting
        Amortized O(1) push/pop cost
        O(n) space complexity, array is always at least 33% full
        Only dynamic growing is supported, however same idea for shrinking
        """

        for i in range(3):
            if self.counts[i] == self.range[i]:
                self.range[i] *= 3

        # resize array dynamically
        if sum(self.counts[i] for i in range(3)) > len(self.array):
            old_starts = copy(self.start)
            count = 0
            for i in range(3):
                self.start[i] = count
                count += self.counts[i]

            array = [0] * count
            for i in range(3):
                for j in range(self.counts[i]):
                    array[self.counts[i] + j] = self.array[old_starts[i] + j]
