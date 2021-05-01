"""
Algorithm practice for strings
"""
from Solver import Solver


class UniqueChar(Solver):

    def solve(self, string):
        """
        Determine if every character in string is unique
        """
        char_set = {s for s in string}
        return len(string) == len(char_set)

    def __init__(self):
        super().__init__()
        self.test_cases = [
            ({'string': 'tes'}, True),
            ({'string': 'nen'}, False)
        ]


class Permutation(Solver):

    def solve(self, s1, s2):
        """
        determine if one of the strings is permutation of the other
        """

        # must be same length to be permutation
        if len(s2) != len(s2):
            return False

        s1_counter = self.char_counter(s1)
        s2_counter = self.char_counter(s2)

        # Must be equal for every value
        for char in s1_counter:
            if s1_counter[char] != s2_counter[char]:
                return False

        return True

    @staticmethod
    def char_counter(string):
        from collections import defaultdict

        counter = defaultdict(int)
        for char in string:
            counter[char] += 1

        return counter

    def __init__(self):
        super().__init__()
        self.test_cases = [
            ({
                 's1': 'alac',
                 's2': 'cala'
             }, True),
            ({
                 's1': 'alice',
                 's2': 'cala'
             }, False)
        ]


if __name__ == '__main__':
    UniqueChar().run_cases()
    Permutation().run_cases()
