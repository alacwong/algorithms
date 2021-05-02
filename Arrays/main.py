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


class Urlfy(Solver):

    def solve(self, string):
        ans = ''
        sub = ''

        for char in string:
            if char != ' ':
                sub += char
            elif sub == '':
                continue
            else:
                ans += f'{sub}%20'
                sub = ''

        return ans + sub

    def __init__(self):
        super().__init__()
        self.test_cases = [
            ({'string': 'mr jam'}, 'mr%20jam'),
            ({'string': 'mr   jam'}, 'mr%20jam'),
            ({'string': 'mr   jam '}, 'mr%20jam%20'),
            ({'string': 'mr   jam is me'}, 'mr%20jam%20is%20me'),
            ({'string': 'mrjam'}, 'mrjam')
        ]


class PalindromePermutation(Solver):

    def solve(self, string):
        """Check if string is a permutation of a palindrome"""

        counter = self.count_chars(string)

        if len(string) % 2 == 0:
            for char in counter:
                if counter[char] % 2 == 1:
                    return False
        else:
            flag = False
            for char in counter:
                if counter[char] % 2 == 1 and not flag:
                    flag = True
                elif counter[char] % 2 == 1 and flag:
                    return False
        return True

    def __init__(self):
        super().__init__()
        self.test_cases = [
            ({'string': 'anna'}, True),
            ({'string': 'nana'}, True),
            ({'string': 'anpna'}, True),
            ({'string': 'nanaz'}, True),
            ({'string': 'fake'}, False),
        ]

    @staticmethod
    def count_chars(string):
        from collections import defaultdict

        counter = defaultdict(int)
        for char in string:
            counter[char] += 1

        return counter


if __name__ == '__main__':
    UniqueChar().run_cases()
    Permutation().run_cases()
    Urlfy().run_cases()
    PalindromePermutation().run_cases()
