from abc import ABC, abstractmethod


class Solver(ABC):

    def __init__(self):
        self.test_cases = []

    @abstractmethod
    def solve(self, **kwargs):
        pass

    def run_cases(self):

        print(f'Running tests for {self.__class__.__name__}')

        for case, ans in self.test_cases:
            my_ans = self.solve(**case)
            if my_ans == ans:
                print('Pass')
            else:
                print(f'Fail: Expected {ans} got {my_ans}')
