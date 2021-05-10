"""
Algorithm practice for strings
"""
from solver import Solver


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


class OneEditAway(Solver):

    def solve(self, s1: str, s2: str):
        """
        Determine if s1 is one edit away form s2
        """

        diff = 0
        if len(s1) == len(s2):  # equal case, check that str diff is < 1
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    diff += 1

        elif len(s1) == len(s2) + 1 or len(s1) + 1 == len(s2):  # case, str length differ by 1
            if len(s2) > len(s1):
                s1, s2 = s2, s1
            i, j = 0, 0

            while i < len(s1) and j < len(s2):
                if s1[i] != s2[j]:
                    diff += 1
                    i += 1
                else:
                    i, j = i + 1, j + 1
        else:
            return False

        return diff < 2

    def __init__(self):
        super().__init__()
        self.test_cases = [
            ({'s1': 'pale', 's2': 'ple'}, True),
            ({'s1': 'page', 's2': 'pale'}, True),
            ({'s1': 'pale', 's2': 'pale'}, True),
            ({'s1': 'pale', 's2': 'qwifqwfiqw'}, False),
            ({'s1': 'pale', 's2': 'pls'}, False),
        ]


class StringCompression(Solver):

    def solve(self, s: str):
        """ Basic string compression
        aabbssssf -> a2b2s4f1
        """
        count, prev, ans = 0, '', ''
        for char in s:
            if char == prev:
                count += 1
            else:
                if count > 0:
                    ans += f'{prev}{count}'
                prev, count = char, 1
        if count:
            ans += f'{prev}{count}'
        return ans if len(ans) < len(s) else s

    def __init__(self):
        super().__init__()
        self.test_cases = [
            ({'s': 'aabbssssf'}, 'a2b2s4f1'),
            ({'s': 'abcde'}, 'abcde'),
            ({'s': ''}, '')
        ]


class RotateMatrix(Solver):

    def solve(self, matrix):
        """
        Rotate a matrix
        [[1 0]  -> [[1 1]
         [1 1]]     [1 0]]
        """

        if len(matrix) == 0:
            return []

        ans = []
        n = len(matrix)
        for i in range(n):
            row = []
            for j in range(n):
                row.append(matrix[j][i])
            ans.append(row)
        return ans


class ZeroMatrix(Solver):

    def solve(self, matrix):
        """Zero out rows with zeros"""
        ans = []
        for index, row in enumerate(matrix):
            for cell in row:
                if cell == 0:
                    ans.append([0] * len(matrix))
                    break
            if len(ans) == index:
                ans.append(row[:])
        return ans


if __name__ == '__main__':
    UniqueChar().run_cases()
    Permutation().run_cases()
    Urlfy().run_cases()
    PalindromePermutation().run_cases()
    OneEditAway().run_cases()
    StringCompression().run_cases()
